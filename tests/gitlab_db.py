import psycopg2

from testing.postgresql import PostgresqlFactory

def gitlab_init(tempdb):
    conn = psycopg2.connect(**tempdb.dsn())
    with conn:
        with conn.cursor() as cur:
            _create_schema(cur)
            _insert_fixtures(cur)

    conn.close()

def _create_schema(cursor):
    cursor.execute(
        'create table namespaces('
        'id int primary key, '
        'path varchar, '
        'parent_id int'
        ')')
    cursor.execute(
        'create table projects('
        'id int primary key, '
        'path varchar, '
        'namespace_id int, '
        'repository_storage varchar'
        ')')
    cursor.execute(
        'create table ci_pipelines('
        'id int primary key, '
        'project_id int, '
        'created_at timestamp, '
        'status varchar'
        ')')
    cursor.execute(
        'create table ci_stages('
        'id int primary key, '
        'pipeline_id int'
        ')')
    cursor.execute(
        'create table ci_builds('
        'id int primary key, '
        'project_id int, '
        'stage_id int, '
        'name varchar, '
        'created_at timestamp, '
        'ref varchar, '
        'tag bool, '
        'status varchar, '
        'allow_failure bool, '
        'artifacts_expire_at timestamp'
        ')')
    cursor.execute(
        'create table ci_job_artifacts('
        'id int primary key, '
        'project_id int, '
        'job_id int, '
        'file_type smallint, '
        'size bigint'
        ')')


def _insert_fixtures(cursor):
    cursor.execute(
        "insert into namespaces(id, path, parent_id) values "
        "(1, 'awesome-people', NULL), "
        "(2, 'go-further', 1), "
        "(3, 'into-the-future-of', 2), "
        "(4, 'cool-projects', NULL), "
        "(5, 'boring-projects', NULL), "
        "(6, 'open-source', 1),"
        "(7, 'open-source', NULL)"
        )
    cursor.execute(
        'cluster namespaces using namespaces_pkey'
        )
    cursor.execute(
        "insert into projects(id, path, namespace_id, repository_storage) values "
        "(1, 'awesome-prod', 1, 'default'),"
        "(2, 'other-cool.project.txt_', 1, 'default'),"
        "(3, 'awesome', 3, 'default'),"
        "(4, 'drilling', 5, 'default'),"
        "(5, 'tunneling', 5, 'default'),"
        "(6, 'carpenter_bees', 5, 'default'),"
        "(7, 'no-gitlab-ci', 1, 'default'),"
        "(8, 'no-artifacts', 1, 'default'),"
        "(9, 'main-project', 7, 'default'),"
        "(10, 'inner-project', 6, 'default')"
        )

    cursor.execute(
        "insert into ci_builds"
        "   (id, project_id, stage_id, name, created_at, ref, tag, status, "
        "    allow_failure, artifacts_expire_at) values "

        # main project that includes old, new, lastgood, orphaned, all failed, tagged, expiring
        "(1, 1,1,  'build', '9/1/2018 4:00:00AM', 'master',    false, 'success', false, NULL),"
        "(2, 1,1,  'test',  '9/1/2018 4:00:00AM', 'master',    false, 'failed',  false, NULL),"
        "(3, 1,2,  'build', '9/1/2018 5:00:00AM', 'master',    false, 'success', false, NULL),"
        "(4, 1,2,  'test',  '9/1/2018 5:00:00AM', 'master',    false, 'failed',  false, NULL),"
        "(5, 1,2,  'test',  '9/1/2018 5:00:00AM', 'master',    false, 'failed',  false, NULL),"
        "(6, 1,2,  'test',  '9/1/2018 5:00:00AM', 'master',    false, 'failed',  false, NULL),"
        "(7, 1,3,  'build', '9/1/2018 5:01:04AM', 'master',    false, 'success', false, NULL),"
        "(8, 1,3,  'test',  '9/1/2018 5:01:04AM', 'master',    false, 'success', false, NULL),"
        "(9, 1,4,  'build', '9/1/2018 6:03:21AM', '2.1.9',     true,  'success', false, NULL),"
        "(10,1,4,  'test',  '9/1/2018 6:07:09AM', '2.1.9',     true,  'success', false, NULL),"
        "(11,1,5,  'build', '9/1/2018 7:01:01AM', 'add-thing', false, 'success', false, NULL),"
        "(12,1,5,  'test',  '9/1/2018 7:01:01AM', 'add-thing', false, 'success', false, NULL),"
        "(13,1,6,  'build', '9/1/2018 8:00:01AM', 'master',    false, 'success', false, NULL),"
        "(14,1,6,  'test',  '9/1/2018 8:00:02AM', 'master',    false, 'failed',  false, NULL),"
        "(15,1,7,  'build', '9/1/2018 9:05:22AM', 'not-good',  false, 'failed',  false, NULL),"
        "(16,1,7,  'test',  '9/1/2018 9:05:23AM', 'not-good',  false, 'failed',  false, NULL),"
        "(17,1,8,  'build', '9/2/2018 1:11:06AM', 'not-good',  false, 'failed',  false, NULL),"
        "(18,1,8,  'test',  '9/2/2018 1:55:12AM', 'not-good',  false, 'failed',  false, NULL),"
        "(19,1,9,  'build', '9/2/2018 2:00:01AM', 'not-good',  false, 'failed',  false, NULL),"
        "(20,1,9,  'test',  '9/2/2018 2:00:02AM', 'not-good',  false, 'failed',  false, NULL),"
        "(21,1,10, 'build', '9/1/2018 7:00:01AM', '7-merged',  false, 'success', false, NULL),"
        "(22,1,10, 'test',  '9/1/2018 7:00:02AM', '7-merged',  false, 'failed',  false, NULL),"
        "(23,1,11, 'build', '9/1/2018 8:05:01AM', '7-merged',  false, 'success', false, NULL),"
        "(24,1,11, 'test',  '9/1/2018 8:05:01AM', '7-merged',  false, 'failed',  false, NULL),"
        "(25,1,11, 'test',  '9/1/2018 8:06:01AM', '7-merged',  false, 'failed',  false, NULL),"
        "(26,1,11, 'test',  '9/1/2018 8:07:01AM', '7-merged',  false, 'failed',  false, NULL),"
        "(27,1,11, 'test',  '9/1/2018 8:08:01AM', '7-merged',  false, 'failed',  false, NULL),"
        "(28,1,12, 'build', '9/1/2018 1:09:01PM', '7-merged',  false, 'success', false, NULL),"
        "(29,1,12, 'test',  '9/1/2018 1:09:01PM', '7-merged',  false, 'success', false, NULL),"
        "(30,1,13, 'build', '9/1/2018 1:00:00PM', 'on-sched',  false, 'success', false, "
        "                                                               '9/2/2018 1:00:00PM'),"
        "(31,1,13, 'test',  '9/1/2018 2:00:00PM', 'on-sched',  false, 'success', false, "
        "                                                               '9/2/2018 1:00:00PM'),"
        "(32,1,14, 'build', '9/1/2018 3:00:00PM', 'on-sched',  false, 'success', false, "
        "                                                               '9/2/2018 1:00:00PM'),"
        "(33,1,14, 'test',  '9/1/2018 4:00:00PM', 'on-sched',  false, 'success', false, "
        "                                                               '9/2/2018 1:00:00PM'),"

        # project that has CI, but no artifacts
        "(34,8,15, 'build', '9/1/2018 1:08:01PM', 'master',  false, 'failed',  false, NULL),"
        "(35,8,15, 'test',  '9/1/2018 1:08:01PM', 'master',  false, 'failed',  false, NULL),"
        "(36,8,16, 'build', '9/1/2018 1:09:01PM', 'master',  false, 'success', false, NULL),"
        "(37,8,16, 'test',  '9/1/2018 1:09:01PM', 'master',  false, 'failed',  false, NULL),"
        "(38,8,16, 'test',  '9/1/2018 1:10:01PM', 'master',  false, 'failed',  false, NULL),"
        "(39,8,16, 'test',  '9/1/2018 1:11:01PM', 'master',  false, 'failed',  false, NULL),"
        "(40,8,17, 'build', '9/1/2018 1:12:01PM', 'master',  false, 'success', false, NULL),"
        "(41,8,17, 'test',  '9/1/2018 1:12:01PM', 'master',  false, 'success', false, NULL),"
        "(42,8,18, 'build', '9/1/2018 1:13:01PM', '1.0.0',   true,  'success', false, NULL),"
        "(43,8,18, 'test',  '9/1/2018 1:13:01PM', '1.0.0',   true,  'success', false, NULL),"

        # project that has regular failures
        "(44,2,19, 'build', '9/1/2018 1:08:01PM', 'master',  false, 'success', false, NULL),"
        "(45,2,19, 'test1', '9/1/2018 1:08:02PM', 'master',  false, 'success', false, NULL),"
        "(46,2,19, 'test2', '9/1/2018 1:08:03PM', 'master',  false, 'failed',  false, NULL),"
        "(47,2,19, 'test3', '9/1/2018 1:08:04PM', 'master',  false, 'success', false, NULL),"
        "(48,2,20, 'build', '9/1/2018 2:08:01PM', 'master',  false, 'success', false, NULL),"
        "(49,2,20, 'test1', '9/1/2018 2:08:02PM', 'master',  false, 'failed',  false, NULL),"
        "(50,2,20, 'test2', '9/1/2018 2:08:03PM', 'master',  false, 'success', false, NULL),"
        "(51,2,20, 'test3', '9/1/2018 2:08:04PM', 'master',  false, 'success', false, NULL),"
        "(52,2,21, 'build', '9/1/2018 3:10:01PM', 'master',  false, 'success', false, NULL),"
        "(53,2,21, 'test1', '9/1/2018 3:08:02PM', 'master',  false, 'success', false, NULL),"
        "(54,2,21, 'test2', '9/1/2018 3:08:03PM', 'master',  false, 'success', false, NULL),"
        "(55,2,21, 'test3', '9/1/2018 3:08:04PM', 'master',  false, 'success', false, NULL),"
        "(56,2,22, 'build', '9/1/2018 4:08:01PM', 'master',  false, 'success', false, NULL),"
        "(57,2,22, 'test1', '9/1/2018 4:08:02PM', 'master',  false, 'failed',  false, NULL),"
        "(58,2,22, 'test2', '9/1/2018 4:08:03PM', 'master',  false, 'failed',  false, NULL),"
        "(59,2,22, 'test3', '9/1/2018 4:08:04PM', 'master',  false, 'failed',  false, NULL),"
        "(60,2,23, 'build', '9/1/2018 5:08:01PM', 'master',  false, 'success', false, NULL),"
        "(61,2,23, 'test1', '9/1/2018 5:08:02PM', 'master',  false, 'success', false, NULL),"
        "(62,2,23, 'test2', '9/1/2018 5:08:03PM', 'master',  false, 'success', false, NULL),"
        "(63,2,23, 'test3', '9/1/2018 5:08:04PM', 'master',  false, 'failed',  false, NULL),"

        # nested project
        "(64,3,24, 'build', '9/1/2018 1:22:03AM', 'master',  false, 'success', false, NULL),"
        "(65,3,25, 'build', '9/1/2018 2:13:04AM', 'master',  false, 'failed',  false, NULL),"
        "(66,3,26, 'build', '9/1/2018 2:38:03AM', 'master',  false, 'success', false, NULL),"
        "(67,3,27, 'build', '9/1/2018 3:42:04AM', 'master',  false, 'success', false, NULL),"
        "(68,3,28, 'build', '9/1/2018 5:59:03AM', 'master',  false, 'success', false, NULL),"
        "(69,3,29, 'build', '9/1/2018 8:01:04AM', 'master',  false, 'success', false, NULL),"
        "(70,3,30, 'build', '9/1/2018 8:17:03AM', 'master',  false, 'success', false, NULL),"
        "(71,3,31, 'build', '9/1/2018 9:08:04AM', 'master',  false, 'failed',  false, NULL),"

        # similar names
        "(72,9,32, 'build', '9/1/2018 1:22:03AM', 'master',  false, 'success', false, NULL),"
        "(73,9,33, 'build', '9/1/2018 2:13:04AM', 'master',  false, 'failed',  false, NULL),"
        "(74,10,34,'build', '9/1/2018 1:22:03AM', 'master',  false, 'success', false, NULL),"
        "(75,10,35,'build', '9/1/2018 2:13:04AM', 'master',  false, 'failed',  false, NULL)"

        )

    # create a pipeline for each job
    cursor.execute(
        "insert into ci_pipelines(id, project_id, created_at, status) "
        "select distinct b.stage_id, b.project_id, b.created_at, "
        "  case when not exists ("
        "         select 1 from ci_builds "
        "         where status='failed' and stage_id=b.stage_id) then 'success' "
        "  else 'failed' end as status "
        "from ci_builds as b "
        "where name='build'"
        )
    # create a stage for each job
    cursor.execute(
        "insert into ci_stages "
        "select distinct stage_id, stage_id as pipeline_id "
        "from ci_builds"
        )

    # create artifacs for each job
    cursor.execute(
        "insert into ci_job_artifacts "
        "select b.id, p.project_id, b.id, 1 as file_type, 491286 as size "
        "from ci_builds as b "
        "join ci_stages as c on c.id=b.stage_id "
        "join ci_pipelines as p on p.id=c.pipeline_id "
        "where b.project_id not in (8)"
        )

gitlab_db = PostgresqlFactory(
    cache_initialized_db=True,
    on_initialized=gitlab_init
    )
