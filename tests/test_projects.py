import psycopg2
import unittest

from .gitlab_db import gitlab_db

from glartifacts.projects import *
from glartifacts.errors import NoProjectError

def project_exists(projects, path):
    return path in [
        '/'.join((p['namespace'],p['project']))
        for p in projects
        ]

class TestProjects(unittest.TestCase):
    def setUp(self):
        self.postgres = gitlab_db()
        self.db = psycopg2.connect(**self.postgres.dsn())

    def tearDown(self):
        self.postgres.stop()

    def test_should_find_project(self):
        project = find_project(self.db, 'awesome-people/awesome-prod')
        self.assertIsNotNone(project)
        self.assertEqual(1, project.project_id)
        self.assertEqual('awesome-people/awesome-prod', project.full_path)
        self.assertEqual('awesome-people/awesome-prod.git', project.disk_path)
        self.assertEqual('project-1', project.gl_repository)
        self.assertFalse(project.branches)

    def test_should_find_nested_project(self):
        project = find_project(
            self.db,
            'awesome-people/go-further/into-the-future-of/awesome')
        self.assertIsNotNone(project)
        self.assertEqual(3, project.project_id)
        self.assertEqual(
            'awesome-people/go-further/into-the-future-of/awesome',
            project.full_path
            )
        self.assertEqual(
            'awesome-people/go-further/into-the-future-of/awesome.git',
            project.disk_path
            )
        self.assertEqual('project-3', project.gl_repository)
        self.assertFalse(project.branches)

    def test_should_not_list_no_artifacts_project(self):
        projects = list_projects(self.db)
        self.assertTrue(projects)
        self.assertFalse(project_exists(projects, 'awesome-people/no-artifacts'))

    def test_should_not_list_no_ci_project(self):
        projects = list_projects(self.db)
        self.assertTrue(projects)
        self.assertFalse(project_exists(projects, 'awesome-people/no-gitlab-ci'))

    def test_should_not_find_project_invalid_name(self):
        with self.assertRaises(NoProjectError):
            find_project(self.db, 'awesome-people/not-awesome')
            find_project(self.db, 'not-awesome-people|awesome-prod')
            find_project(self.db, 'awesome-prod')
            find_project(self.db, '')
            find_project(self.db, None)

    def test_should_list_projects(self):
        projects = list_projects(self.db)
        self.assertTrue(projects)
        self.assertTrue(project_exists(projects, 'awesome-people/awesome-prod'))
        self.assertTrue(project_exists(projects, 'awesome-people/other-cool.project.txt_'))

    def test_should_list_artifact_count(self):
        artifact_counts = {
            'awesome-prod': 33,
            'other-cool.project.txt_': 20,
            'awesome': 8
            }
        projects = list_projects(self.db)
        for p in projects:
            self.assertEqual(artifact_counts[p[1]], p[3])

    def test_should_ishidden(self):
        self.assertTrue(ishidden('._some_job'))
        self.assertTrue(ishidden('.'))
        self.assertTrue(ishidden('...'))
        self.assertTrue(ishidden('.my.job.is.repetitious'))

    def test_should_not_ishidden(self):
        self.assertFalse(ishidden('build'))
        self.assertFalse(ishidden('_build'))
        self.assertFalse(ishidden('b.u.i.l.d.'))
        self.assertFalse(ishidden('b.'))

    def test_should_isreserved(self):
        self.assertTrue(isreserved('image'))
        self.assertTrue(isreserved('Image'))
        self.assertTrue(isreserved('IMAGE'))
        self.assertTrue(isreserved('types'))
        self.assertTrue(isreserved('after_Script'))

    def test_should_not_isreserved(self):
        self.assertFalse(isreserved('vars'))
        self.assertFalse(isreserved('.cache'))
        self.assertFalse(isreserved('_image'))

    def test_should_create_valid_branch_tree_path(self):
        project = find_project(self.db, 'boring-projects/tunneling')
        self.assertIsNotNone(project)

        branch = Branch(project, 'master', 'ab492cf81')
        self.assertEqual(
            branch.tree_path(),
            'boring-projects/tunneling/tree/master'
            )

    def test_should_create_valid_commit_tree_path(self):
        project = find_project(self.db, 'boring-projects/tunneling')
        self.assertIsNotNone(project)

        self.assertEqual(
            project.tree_path('ab492cf81'),
            'boring-projects/tunneling/tree/ab492cf81'
            )
