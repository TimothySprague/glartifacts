import argparse
import os
import psycopg2
import psycopg2.extras
import pwd

from enum import Enum
from . import log
from .utils import indent

class ArchiveStrategy(Enum):
    # Keep good artifacts per-build
    LASTGOOD_BUILD=1

    # Keep good artifacts per-pipeline
    LASTGOOD_PIPELINE=2

def get_archive_strategy_query(strategy):
    if strategy == ArchiveStrategy.LASTGOOD_BUILD:
        return sql_lastgood_build
    elif strategy == ArchiveStrategy.LASTGOOD_PIPELINE:
        return sql_lastgood_pipeline

    raise Exception("Strategy {} not implemented".format(strategy.name))

def list_archive_artifacts(db, project_id, strategy=ArchiveStrategy.LASTGOOD_BUILD):
    strategy_query = get_archive_strategy_query(strategy)
    action_query = sql_artifact_list.format(sql_artifacts)
    sql = strategy_query + action_query
    log.debug("Running %s archive query:\n  %s", strategy.name, indent(sql))

    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql, dict(project_id=tuple(project_id)))

    return cur.fetchall()

def archive_artifacts(db, project_ids, strategy=ArchiveStrategy.LASTGOOD_BUILD):
    strategy_query = get_archive_strategy_query(strategy)
    action_query = sql_artifact_expire.format(sql_artifacts)

    sql = strategy_query + action_query
    log.debug("Running %s archive query:\n  %s", strategy.name, indent(sql))

    cur = db.cursor()
    cur.execute(sql, dict(project_id=tuple(project_ids)))

# Archive artifacts older than the most recent successful pipeline
sql_lastgood_pipeline = """
with lastgood as (
    select b.project_id, b.name,
            max(p.created_at) as pipeline_date, 
	    max(b.created_at) as build_date
    from ci_builds as b
    join ci_stages as s on s.id=b.stage_id
    join ci_pipelines as p on p.id=s.pipeline_id
    where p.status='success' and
	    p.tag=false and
	    b.artifacts_expire_at is null and
            b.project_id in %(project_id)s
    group by b.name, b.project_id
)
"""

# Archive artifacts older than the most recent successful job
sql_lastgood_build = """
with lastgood as (
    select b.project_id, b.name,
            max(p.created_at) as pipeline_date, 
            max(b.created_at) as build_date
    from ci_builds as b
    join ci_stages as s on s.id=b.stage_id
    join ci_pipelines as p on p.id=s.pipeline_id
    where (b.status='success' or b.allow_failure) and 
            b.tag=false and
            b.artifacts_expire_at is null and
            b.project_id in %(project_id)s
    group by b.name, b.project_id
)
"""

sql_artifact_list = """
select a.size, b.name, b.status, b.tag,
    p.created_at as scheduled_at, b.created_at as built_at,
    b.artifacts_expire_at as expire_at
{}
"""

sql_artifact_expire = """
update ci_builds as t
set artifacts_expire_at=(now() at time zone 'utc')
{}
    and t.id=b.id
"""

sql_artifacts = """
from lastgood
join ci_builds as b on b.project_id=lastgood.project_id and b.name=lastgood.name
join ci_stages as s on s.id=b.stage_id
join ci_pipelines as p on p.id=s.pipeline_id
join ci_job_artifacts as a on a.job_id=b.id
where b.created_at<lastgood.build_date
    and p.created_at<=lastgood.pipeline_date
    and b.artifacts_expire_at is null
    and b.tag = false
    and a.file_type = 1
"""
