import enum
import io
import itertools

import psycopg2
import psycopg2.extras

from . import log
from .utils import indent

class ExpirationStrategy(enum.Enum):
    # Keep good artifacts per-job
    LASTGOOD_JOB = 1

    # Keep good artifacts per-pipeline
    LASTGOOD_PIPELINE = 2

    def __str__(self):
        return self.name

    @staticmethod
    def parse(value):
        try:
            return ExpirationStrategy[value]
        except KeyError:
            return None

def _load_project_branches(cursor, projects):
    cursor.execute(
        "create temp table "
        "__project_branch_jobs (id int, ref varchar, job varchar) "
        "on commit drop"
        )

    # Get a flattened list of tab-delimited (project_id, branch_name, job_name) tuples
    items = map(
        lambda p: [
            '{}\t{}\t{}\n'.format(p.id, branch.name, job_name)
            for branch in p.branches
            for job_name in branch.job_names
            ],
        projects.values()
        )
    items = itertools.chain.from_iterable(items)

    # psql copy_from requires a tab-delimited fileobj one row per-line
    data = io.StringIO()
    for row in items:
        data.write(row)
    data.seek(0)

    cursor.copy_from(data, '__project_branch_jobs', columns=('id', 'ref', 'job'))

def get_removal_strategy_query(strategy):
    if strategy == ExpirationStrategy.LASTGOOD_JOB:
        return Query.lastgood.format(Query.good_job)
    elif strategy == ExpirationStrategy.LASTGOOD_PIPELINE:
        return Query.lastgood.format(Query.good_pipeline)

    raise Exception("Strategy {} not implemented".format(strategy.name))

def list_remove_artifacts(db, projects, strategy):
    strategy_query = get_removal_strategy_query(strategy)
    action_query = Query.artifact_list.format(Query.identify_artifacts)
    sql = strategy_query + action_query
    log.debug("Running %s list remove artifacts query:\n  %s", strategy.name, indent(sql))

    with db:
        with db.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            _load_project_branches(cur, projects)
            cur.execute(sql)
            return cur.fetchall()

def remove_artifacts(db, projects, strategy):
    strategy_query = get_removal_strategy_query(strategy)
    action_query = Query.artifact_expire.format(Query.identify_artifacts)

    sql = strategy_query + action_query
    log.debug("Running %s remove artifacts query:\n  %s", strategy.name, indent(sql))

    with db:
        with db.cursor() as cur:
            _load_project_branches(cur, projects)
            cur.execute(sql)

class Query():
    # Find the date of the most recent good pipeline and job
    lastgood = """
with lastgood as (
select lg.project_id, lg.name, lg.ref, lg.pipeline_date,
    max(b.created_at) as build_date
from (
    select b.project_id, b.name, b.ref,
            max(p.created_at) as pipeline_date
    from ci_builds as b
    join __project_branch_jobs as pbj on pbj.id=b.project_id
    join ci_stages as s on s.id=b.stage_id
    join ci_pipelines as p on p.id=s.pipeline_id
    where {}
    group by b.project_id, b.name, b.ref
) as lg
join ci_builds as b on b.project_id=lg.project_id and b.name=lg.name and b.ref=lg.ref
join ci_stages as s on s.id=b.stage_id
join ci_pipelines as p on p.id=s.pipeline_id
where p.created_at = lg.pipeline_date
group by lg.project_id, lg.name, lg.ref, lg.pipeline_date
)
"""

    # Criteria that define "good" for Job or Pipeline
    good_job = "(b.status='success' or b.allow_failure)"
    good_pipeline = "(p.status='success')"

    # Identifies old artifacts based on a lastgood strategy
    # "old" is defined as:
    #    Older than the lastgood pipeline OR
    #       older than the lastgood job within the lastgood pipeline
    #    Not tagged
    #    Not already expired
    #    Has artifacts file_type=1 (zip)
    identify_artifacts = """
from lastgood
join ci_builds as b on b.project_id=lastgood.project_id and b.name=lastgood.name and b.ref=lastgood.ref
join ci_stages as s on s.id=b.stage_id
join ci_pipelines as p on p.id=s.pipeline_id
join ci_job_artifacts as a on a.job_id=b.id
left join __project_branch_jobs as pbj
    on pbj.id=b.project_id and pbj.ref=b.ref and pbj.job=b.name
where (
        p.created_at<lastgood.pipeline_date or
        (p.created_at=lastgood.pipeline_date and b.created_at<lastgood.build_date)
        or pbj.id is NULL
    )
    and b.tag = false
    and b.artifacts_expire_at is null
    and a.file_type = 1
"""

    # Wrapper that lists identified artifacts
    artifact_list = """
select p.id as pipeline_id, coalesce(a.size, 0) as size, b.id as job_id, b.name, b.status,
    b.tag, b.ref,
    p.created_at as scheduled_at, b.created_at as built_at,
    b.artifacts_expire_at as expire_at
{}
"""

    # Wrapper that sets artifact expiration on identified artifacts
    artifact_expire = """
update ci_builds as target
set artifacts_expire_at=(now() at time zone 'utc')
{}
    and target.id=b.id
"""