import argparse
import os
import psycopg2
import psycopg2.extras
import pwd
from .errors import NoProjectError

def get_project_id(db, name, parent_id):
    cur = db.cursor()
    r = cur.execute(sql_get_project, dict(name=name,parent_id=parent_id))
    project = cur.fetchone()
    if not project:
        raise NoProjectError

    return project[0]

def get_namespace_id(db, name, parent_id):
    cur = db.cursor()
    r = cur.execute(sql_get_namespace, dict(name=name,parent_id=parent_id))
    ns = cur.fetchone()
    if not ns:
        raise NoProjectError

    return ns[0]

def walk_namespaces(db, namespaces, project, parent_id=None):
    if not namespaces:
        return get_project_id(db, project, parent_id)

    ns = namespaces.pop(0)
    ns_id = get_namespace_id(db, ns, parent_id)

    return walk_namespaces(db, namespaces, project, ns_id)

def find_project(db, project_path):
    namespaces = project_path.split('/')
    if not namespaces:
        raise NoProjectError

    project = namespaces.pop()

    return walk_namespaces(db,namespaces, project)

def list_projects(db):
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql_projects_with_artifacts)
    
    return cur.fetchall()

def list_artifacts(db, project_path):
    project_id = find_project(db, project_path)
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql_get_artifacts, dict(project_id=project_id))

    return cur.fetchall()

sql_projects_with_artifacts = """
select a.project_id, p.name as project, n.name as namespace, 
    count(distinct a.job_id) as artifact_count
from ci_job_artifacts as a
inner join projects as p on p.id=a.project_id
left join namespaces as n on p.namespace_id=n.id
where a.file_type <> 3
group by a.project_id, p.name, n.name
"""
sql_get_artifacts = """
select a.size, b.name, b.status, b.tag,
    p.created_at as scheduled_at, b.created_at as built_at,
    a.expire_at as expire_at
from ci_job_artifacts as a
inner join ci_builds as b on b.id=a.job_id
inner join ci_stages as s on s.id=b.stage_id
inner join ci_pipelines as p on p.id=s.pipeline_id
where a.project_id=%(project_id)s and a.file_type=1
"""


sql_get_namespace = """
    select id from namespaces where name=%(name)s and
        (%(parent_id)s is null or parent_id=%(parent_id)s)
"""
sql_get_project = """
    select id from projects where name=%(name)s and
        (%(parent_id)s is null or namespace_id=%(parent_id)s)
"""


