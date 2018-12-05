import psycopg2
import psycopg2.extras

from .errors import NoProjectError

class Project(object):
    def __init__(self, id, path, storage):
        self.id = id
        self.storage = storage
        self.full_path = path
        self.disk_path = self.full_path + '.git'
        self.gl_repository = 'project-{}'.format(id)
        self.projects = None

def get_project(db, path, parent_id):
    project = None

    with db:
        with db.cursor() as cur:
            cur.execute(Query.get_project, dict(path=path, parent_id=parent_id))
            project = cur.fetchone()

    if not project:
        raise NoProjectError

    return project

def get_namespace_id(db, path_component, parent_id):
    ns = None
    with db:
        with db.cursor() as cur:
            cur.execute(Query.get_namespace, dict(path=path_component, parent_id=parent_id))
            ns = cur.fetchone()

    if not ns:
        raise NoProjectError

    return ns[0]

def walk_namespaces(db, namespaces, project_path, parent_id=None):
    if not namespaces:
        return get_project(db, project_path, parent_id)

    ns_path = namespaces.pop(0)
    ns_id = get_namespace_id(db, ns_path, parent_id)

    return walk_namespaces(db, namespaces, project_path, ns_id)

def find_project(db, full_path):
    namespaces = full_path.split('/')
    if not namespaces:
        raise NoProjectError

    project_path = namespaces.pop()
    id, storage = walk_namespaces(
            db,
            namespaces,
            project_path)

    return Project(
            id,
            full_path,
            storage
            )

def list_projects(db):
    with db:
        with db.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute(Query.projects_with_artifacts)
            return cur.fetchall()

def list_artifacts(db, project_ids):
    with db:
        with db.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute(Query.get_artifacts, dict(project_id=tuple(project_ids)))
            return cur.fetchall()

class Query():
    projects_with_artifacts = """
with recursive ns_paths(id, parent_id, path) as (
    select n.id, n.parent_id, n.path
        from namespaces as n
        where n.parent_id is NULL
    union all
    select c.id, c.parent_id, (p.path || '/' || c.path) as path
        from namespaces as c
        inner join ns_paths as p on p.id=c.parent_id
)
select a.project_id, p.path as project, n.path as namespace,
    count(distinct a.job_id) as artifact_count
from ci_job_artifacts as a
inner join projects as p on p.id=a.project_id
left join ns_paths as n on p.namespace_id=n.id
where a.file_type <> 3
group by a.project_id, p.path, n.path
"""

    get_artifacts = """
select p.id as pipeline_id, coalesce(a.size, 0) as size, b.name, b.id as job_id, b.status,
    b.tag, b.ref,
    p.created_at as scheduled_at, b.created_at as built_at,
    b.artifacts_expire_at as expire_at
from ci_job_artifacts as a
inner join ci_builds as b on b.id=a.job_id
inner join ci_stages as s on s.id=b.stage_id
inner join ci_pipelines as p on p.id=s.pipeline_id
where a.project_id IN %(project_id)s and a.file_type=1
"""

    get_namespace = """
select id from namespaces where path=%(path)s and
    (%(parent_id)s is null or parent_id=%(parent_id)s)
"""

    get_project = """
select id, repository_storage
from projects
where path=%(path)s and
    (%(parent_id)s is null or namespace_id=%(parent_id)s)
"""
