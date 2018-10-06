import enum

import psycopg2
import psycopg2.extras

from . import log
from .utils import indent

class ArchiveStrategy(enum.Enum):
    # Keep good artifacts per-build
    LASTGOOD_BUILD = 1

    # Keep good artifacts per-pipeline
    LASTGOOD_PIPELINE = 2

    def __str__(self):
        return self.name

    @staticmethod
    def parse(value):
        try:
            return ArchiveStrategy[value]
        except KeyError:
            return None

def get_archive_strategy_query(strategy):
    if strategy == ArchiveStrategy.LASTGOOD_BUILD:
        return Query.lastgood.format(Query.good_build)
    elif strategy == ArchiveStrategy.LASTGOOD_PIPELINE:
        return Query.lastgood.format(Query.good_pipeline)

    raise Exception("Strategy {} not implemented".format(strategy.name))

def list_archive_artifacts(db, project_id, strategy):
    strategy_query = get_archive_strategy_query(strategy)
    action_query = Query.artifact_list.format(Query.identify_artifacts)
    sql = strategy_query + action_query
    log.debug("Running %s archive query:\n  %s", strategy.name, indent(sql))

    with db.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute(sql, dict(project_id=tuple(project_id)))
        return cur.fetchall()

def archive_artifacts(db, project_ids, strategy):
    strategy_query = get_archive_strategy_query(strategy)
    action_query = Query.artifact_expire.format(Query.identify_artifacts)

    sql = strategy_query + action_query
    log.debug("Running %s archive query:\n  %s", strategy.name, indent(sql))

    with db.cursor() as cur:
        cur.execute(sql, dict(project_id=tuple(project_ids)))

class Query():
    # Find the date of the most recent good pipeline and build
    lastgood = """
with lastgood as (
select lg.project_id, lg.name, lg.ref, lg.pipeline_date,
    max(b.created_at) as build_date
from (
    select b.project_id, b.name, b.ref,
            max(p.created_at) as pipeline_date
    from ci_builds as b
    join ci_stages as s on s.id=b.stage_id
    join ci_pipelines as p on p.id=s.pipeline_id
    where b.project_id in %(project_id)s and
        {}
    group by b.project_id, b.name, b.ref
) as lg
join ci_builds as b on b.project_id=lg.project_id and b.name=lg.name and b.ref=lg.ref
join ci_stages as s on s.id=b.stage_id
join ci_pipelines as p on p.id=s.pipeline_id
where p.created_at = lg.pipeline_date
group by lg.project_id, lg.name, lg.ref, lg.pipeline_date
)
"""

    # Criteria that define "good" for Build or Pipeline
    good_build = "(b.status='success' or b.allow_failure)"
    good_pipeline = "(p.status='success')"

    # Identifies old artifacts based on a lastgood strategy
    # "old" is defined as:
    #    Older than the lastgood pipeline OR
    #       older than the lastgood build within the lastgood pipeline
    #    Not tagged
    #    Not already expired
    #    Has artifacts file_type=1 (zip)
    identify_artifacts = """
from lastgood
join ci_builds as b on b.project_id=lastgood.project_id and b.name=lastgood.name and b.ref=lastgood.ref
join ci_stages as s on s.id=b.stage_id
join ci_pipelines as p on p.id=s.pipeline_id
join ci_job_artifacts as a on a.job_id=b.id
where (
        p.created_at<lastgood.pipeline_date or
        (p.created_at=lastgood.pipeline_date and b.created_at<lastgood.build_date)
    )
    and b.tag = false
    and b.artifacts_expire_at is null
    and a.file_type = 1
"""

    # Wrapper that lists identified artifacts
    artifact_list = """
select p.id as pipeline_id, a.size, b.id as job_id, b.name, b.status,
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
