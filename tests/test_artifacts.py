import psycopg2
import unittest

from .gitlab_db import gitlab_db

from glartifacts.artifacts import *
from glartifacts.projects import Project
from glartifacts.utils import *

def project_exists(projects, path):
    return path in [
        '/'.join((p['namespace'],p['project']))
        for p in projects
        ]

def all_strategies():
    return [
        ExpirationStrategy.LASTGOOD_PIPELINE,
        ExpirationStrategy.LASTGOOD_JOB,
        ]

def artifacts_for_project(artifacts, project_id):
    return [a for a in artifacts if a['project_id'] == project_id]

def artifacts_for_job(artifacts, job_id):
    return next((a for a in artifacts if a['job_id'] == job_id))

def artifacts_for_ref(artifacts, ref):
    return [a for a in artifacts if a['ref'] == ref]

class TestProjects(unittest.TestCase):
    def setUp(self):
        self.postgres = gitlab_db()
        self.db = psycopg2.connect(**self.postgres.dsn())

    def tearDown(self):
        self.postgres.stop()

    def _list_projects(self):
        projects = {
            1: Project(1, 'awesome-people/awesome-prod', 'default'),
            2: Project(2, 'awesome-people/other-cool.project.txt_', 'default'),
            3: Project(3, 'awesome-people/go-further/into-the-future-of/awesome', 'default'),
            4: Project(4, 'boring-projects/drilling', 'default'),
            5: Project(5, 'boring-projects/tunneling', 'default'),
            6: Project(6, 'boring-projects/carpenter_bees', 'default'),
            7: Project(7, 'awesome-people/no-gitlab-ci', 'default'),
            8: Project(8, 'awesome-people/no-artifacts', 'default'),
            9: Project(9, 'open-source/main-project', 'default'),
            10: Project(10, 'awesome-people/open-source/inner-project', 'default'),
            }

        # Add non-master, non-merged branches
        projects[1].add_branch('add-thing', '1')
        projects[1].add_branch('not-good', '1')
        projects[1].add_branch('on-sched', '1')

        for p in projects.values():
            # everyone has master
            p.add_branch('master', '1')
            for b in p.branches:
                b.job_names = ['build', 'test', 'test1', 'test2']

        return projects

    def all_artifacts(self, strategy):
        projects = self._list_projects()

        artifacts = list_artifacts(
            self.db,
            projects,
            strategy,
            )
        self.assertIsNotNone(artifacts)
        self.assertEqual(65, len(artifacts))

        return artifacts

    def all_artifacts_are(self, artifacts, state):
        for a in artifacts:
            self.assertEqual(
                state,
                ArtifactDisposition(a['disposition']),
                'artifacts for job {} are not {}'.format(
                    a['job_id'],
                    state
                    )
                )

    def no_artifacts_are(self, artifacts, state, exceptions=None):
        for a in artifacts:
            if exceptions and a in exceptions:
                continue

            self.assertNotEqual(
                state,
                ArtifactDisposition(a['disposition']),
                'artifacts for job {} are {}'.format(
                    a['job_id'],
                    state
                    )
                )

    def test_scheduled_artifacts_are_expiring(self):
        for strategy in all_strategies():
            artifacts = self.all_artifacts(strategy)

            sched_artifacts = artifacts_for_ref(artifacts, 'on-sched')
            self.assertEqual(4, len(sched_artifacts))
            self.all_artifacts_are(sched_artifacts, ArtifactDisposition.EXPIRING)

            self.no_artifacts_are(
                artifacts,
                ArtifactDisposition.EXPIRING,
                exceptions=sched_artifacts,
                )

    def test_deleted_branch_or_job_artifacts_are_orphaned(self):
        job_ids = list(itertools.chain(*[
            [63], [59], [55], [51], [47], range(21,30)
            ]))
        for strategy in all_strategies():
            artifacts = self.all_artifacts(strategy)

            orphaned = [artifacts_for_job(artifacts, a) for a in job_ids]
            self.assertEqual(len(job_ids), len(orphaned))
            self.all_artifacts_are(orphaned, ArtifactDisposition.ORPHANED)

            self.no_artifacts_are(
                artifacts,
                ArtifactDisposition.ORPHANED,
                exceptions=orphaned,
                )

    def test_tagged_artifacts_are_tagged(self):
        job_ids = [10,9]
        for strategy in all_strategies():
            artifacts = self.all_artifacts(strategy)

            tagged = [artifacts_for_job(artifacts, a) for a in job_ids]
            self.assertEqual(len(job_ids), len(tagged))
            self.all_artifacts_are(
                tagged,
                ArtifactDisposition.TAGGED
                )

            self.no_artifacts_are(
                artifacts,
                ArtifactDisposition.TAGGED,
                exceptions=tagged,
                )

    def test_lastgood_pipeline_artifacts_are_lastgood(self):
        artifacts = self.all_artifacts(
            ExpirationStrategy.LASTGOOD_PIPELINE,
            )

        job_ids = list(itertools.chain(*[
            [70, 72, 74],
            range(52, 55),
            [11, 12],
            [7,8],
            ]))
        lastgood = [artifacts_for_job(artifacts, a) for a in job_ids]
        self.assertEqual(len(job_ids), len(lastgood))
        self.all_artifacts_are(lastgood, ArtifactDisposition.GOOD)

        self.no_artifacts_are(
            artifacts,
            ArtifactDisposition.GOOD,
            exceptions=lastgood,
            )

    def test_lastgood_job_artifacts_are_lastgood(self):
        artifacts = self.all_artifacts(
            ExpirationStrategy.LASTGOOD_JOB,
            )

        job_ids = list(itertools.chain(*[
            [70,72,74],
            range(60,63),
            range(11, 14),
            [8],
            ]))
        lastgood = [artifacts_for_job(artifacts, a) for a in job_ids]
        self.assertEqual(len(job_ids), len(lastgood))
        self.all_artifacts_are(lastgood, ArtifactDisposition.GOOD)

        self.no_artifacts_are(
            artifacts,
            ArtifactDisposition.GOOD,
            exceptions=lastgood,
            )

    def test_newer_than_lastgood_pipeline_artifacts_are_new(self):
        artifacts = self.all_artifacts(
            ExpirationStrategy.LASTGOOD_PIPELINE,
            )

        job_ids = list(itertools.chain(*[
            [71,73,75],
            range(60,63),
            range(56,59),
            range(13,21)
            ]))
        new_artifacts = [artifacts_for_job(artifacts, a) for a in job_ids]
        self.assertEqual(len(job_ids), len(new_artifacts))
        self.all_artifacts_are(new_artifacts, ArtifactDisposition.NEW)

        self.no_artifacts_are(
            artifacts,
            ArtifactDisposition.NEW,
            exceptions=new_artifacts,
            )

    def test_newer_than_lastgood_job_artifacts_are_new(self):
        artifacts = self.all_artifacts(
            ExpirationStrategy.LASTGOOD_JOB,
            )

        job_ids = list(itertools.chain(*[
            [71,73,75],
            range(14,21)
            ]))
        new_artifacts = [artifacts_for_job(artifacts, a) for a in job_ids]
        self.assertEqual(len(job_ids), len(new_artifacts))
        self.all_artifacts_are(new_artifacts, ArtifactDisposition.NEW)

        self.no_artifacts_are(
            artifacts,
            ArtifactDisposition.NEW,
            exceptions=new_artifacts,
            )

    def test_older_than_lastgood_pipeline_artifacts_are_old(self):
        artifacts = self.all_artifacts(
            ExpirationStrategy.LASTGOOD_PIPELINE,
            )

        job_ids = list(itertools.chain(*[
            range(1,7),
            range(44,47),
            range(48,51),
            range(64,70),
            ]))
        old_artifacts = [artifacts_for_job(artifacts, a) for a in job_ids]
        self.assertEqual(len(job_ids), len(old_artifacts))
        self.all_artifacts_are(old_artifacts, ArtifactDisposition.OLD)

        self.no_artifacts_are(
            artifacts,
            ArtifactDisposition.OLD,
            exceptions=old_artifacts,
            )

    def test_older_than_lastgood_job_artifacts_are_old(self):
        artifacts = self.all_artifacts(
            ExpirationStrategy.LASTGOOD_JOB,
            )

        job_ids = list(itertools.chain(*[
            range(1,8),
            range(44,47),
            range(48,51),
            range(52,55),
            range(56,59),
            range(64,70),
            ]))
        old_artifacts = [artifacts_for_job(artifacts, a) for a in job_ids]
        self.assertEqual(len(job_ids), len(old_artifacts))
        self.all_artifacts_are(old_artifacts, ArtifactDisposition.OLD)

        self.no_artifacts_are(
            artifacts,
            ArtifactDisposition.OLD,
            exceptions=old_artifacts,
            )


    def test_should_list_lastgood_pipeline_remove_artifacts(self):
        projects = self._list_projects()
        artifacts = list_artifacts(
            self.db,
            projects,
            ExpirationStrategy.LASTGOOD_PIPELINE,
            remove_only=True
            )

        job_ids = list(itertools.chain(*[
            #old
            range(1,7),
            range(44,47),
            range(48,51),
            range(64,70),
            # orphans
            [63], [59], [55], [51], [47],
            range(21,30)
            ]))
        remove_artifacts = [artifacts_for_job(artifacts, a) for a in job_ids]
        self.assertEqual(len(job_ids), len(remove_artifacts))
        self.no_artifacts_are(
            artifacts,
            ArtifactDisposition.OLD,
            exceptions=remove_artifacts,
            )

        self.no_artifacts_are(
            artifacts,
            ArtifactDisposition.ORPHANED,
            exceptions=remove_artifacts,
            )

        self.assertEqual(len(remove_artifacts), len(artifacts))

    def test_should_list_lastgood_job_remove_artifacts(self):
        projects = self._list_projects()
        artifacts = list_artifacts(
            self.db,
            projects,
            ExpirationStrategy.LASTGOOD_JOB,
            remove_only=True
            )

        job_ids = list(itertools.chain(*[
            #old
            range(1,8),
            range(44,47),
            range(48,51),
            range(52,55),
            range(56,59),
            range(64,70),
            # orphans
            [63], [59], [55], [51], [47],
            range(21,30)
            ]))
        remove_artifacts = [artifacts_for_job(artifacts, a) for a in job_ids]
        self.assertEqual(len(job_ids), len(remove_artifacts))
        self.no_artifacts_are(
            artifacts,
            ArtifactDisposition.OLD,
            exceptions=remove_artifacts,
            )

        self.no_artifacts_are(
            artifacts,
            ArtifactDisposition.ORPHANED,
            exceptions=remove_artifacts,
            )

        self.assertEqual(len(remove_artifacts), len(artifacts))

    def test_should_remove_lastgood_pipeline_old_and_orphans(self):
        projects = self._list_projects()
        remove_artifacts(
            self.db,
            projects,
            ExpirationStrategy.LASTGOOD_PIPELINE,
            )

        artifacts = list_artifacts(
            self.db,
            projects,
            ExpirationStrategy.LASTGOOD_PIPELINE,
            )

        job_ids = list(itertools.chain(*[
            #old
            range(1,7),
            range(44,47),
            range(48,51),
            range(64,70),
            # orphans
            [63], [59], [55], [51], [47],
            range(21,30),
            # prior expiring
            range(30, 34),
            ]))

        expiring_artifacts = [artifacts_for_job(artifacts, a) for a in job_ids]
        self.assertEqual(len(job_ids), len(expiring_artifacts))
        self.all_artifacts_are(
            expiring_artifacts,
            ArtifactDisposition.EXPIRING,
            )

        self.no_artifacts_are(
            artifacts,
            ArtifactDisposition.EXPIRING,
            exceptions=expiring_artifacts,
            )

    def test_should_remove_lastgood_job_old_and_orphans(self):
        projects = self._list_projects()
        remove_artifacts(
            self.db,
            projects,
            ExpirationStrategy.LASTGOOD_JOB,
            )

        artifacts = list_artifacts(
            self.db,
            projects,
            ExpirationStrategy.LASTGOOD_JOB,
            )

        job_ids = list(itertools.chain(*[
            #old
            range(1,8),
            range(44,47),
            range(48,51),
            range(52,55),
            range(56,59),
            range(64,70),
            # orphans
            [63], [59], [55], [51], [47],
            range(21,30),
            # prior expiring
            range(30, 34),
            ]))

        expiring_artifacts = [artifacts_for_job(artifacts, a) for a in job_ids]
        self.assertEqual(len(job_ids), len(expiring_artifacts))
        self.all_artifacts_are(
            expiring_artifacts,
            ArtifactDisposition.EXPIRING,
            )

        self.no_artifacts_are(
            artifacts,
            ArtifactDisposition.EXPIRING,
            exceptions=expiring_artifacts,
            )
