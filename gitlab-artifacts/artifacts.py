import argparse
import os
import psycopg2
import psycopg2.extras
import pwd

LASTKNOWNGOOD_BUILD=1
LASTKNOWNGOOD_PIPELINE=2

def get_archive_strategy_query(strategy):
    if strategy == LASTKNOWNGOOD_BUILD:
        return sql_lkg_build

    raise Exception("Strategy {} not implemented".format(strategy))

def list_archive_artifacts(db, project_id, archive_strategy=LASTKNOWNGOOD_BUILD):
    strategy_query = get_archive_strategy_query(archive_strategy)

    sql = strategy_query + sql_list_artifacts
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql, dict(project_id=project_id))

    return cur.fetchall()

sql_lkg_pipeline = """
with lkg as (
    select b.project_id, b.name,
            max(p.created_at) as last_pipeline, 
	    max(b.created_at) as last_build
    from ci_builds as b
    join ci_stages as s on s.id=b.stage_id
    join ci_pipelines as p on p.id=s.pipeline_id
    where p.status='success' and
	    p.tag=false and
	    b.artifacts_expire_at is null
    group by b.name, b.project_id
)
"""

sql_lkg_build = """
with lkg as (
    select b.project_id, b.name,
            max(p.created_at) as last_pipeline, 
            max(b.created_at) as last_build
    from ci_builds as b
    join ci_stages as s on s.id=b.stage_id
    join ci_pipelines as p on p.id=s.pipeline_id
    where (b.status='success' or b.allow_failure) and 
            b.tag=false and
            b.artifacts_expire_at is null
    group by b.name, b.project_id
)
"""

sql_list_artifacts = """
select a.size, b.name, b.status, b.tag,
    p.created_at as scheduled_at, b.created_at as built_at,
    a.expire_at
from lkg
join ci_builds as b on b.project_id=lkg.project_id and b.name=lkg.name
join ci_stages as s on s.id=b.stage_id
join ci_pipelines as p on p.id=s.pipeline_id
join ci_job_artifacts as a on a.job_id=b.id
where b.created_at<lkg.last_build and
	p.created_at<=lkg.last_pipeline and
        b.artifacts_expire_at is null and
        b.tag = false and
        a.file_type = 1
"""

sql_archive_artifacts = """
update ci_builds as b
set artifacts_expire_at=(now() at time zone 'utc')
from lkg
join ci_builds as b on b.project_id=lkg.project_id and b.name=lkg.name
join ci_stages as s on s.id=b.stage_id
join ci_pipelines as p on p.id=s.pipeline_id
where b.created_at<lkg.last_build and
	p.created_at<=lkg.last_pipeline
"""

