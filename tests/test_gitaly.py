import unittest

from collections import namedtuple
from unittest import mock

from glartifacts.gitaly import GitalyClient
from glartifacts.projects import Project

BranchTarget = namedtuple('Target', 'id')
Branch = namedtuple('Branch', 'name target')
BranchResponse = namedtuple('BranchPage', 'branches')

class TestGitaly(unittest.TestCase):

    def _make_branch_response(self, branches):
        branches = [
            Branch._make([name, BranchTarget._make([i])])
            for i, name in enumerate(branches)
            ]
        return BranchResponse._make([branches])

    @mock.patch('glartifacts.gitaly.proto.ref_pb2_grpc.RefServiceStub')
    def test_should_find_branches_with_slashes(self, mock_refsvc):
        mock_refsvc.return_value.FindAllBranches.return_value = [
                self._make_branch_response([
                    b'open-source/crazy-names/master',
                    b'open-source/crazy-names/release/v2',
                    ])
                ]

        project = Project(11, 'open-source/crazy-names', 'default')
        with GitalyClient() as gitaly:
            branches = gitaly.get_branches(project)

            self.assertEqual(2, len(branches))
            self.assertEqual('master', branches[0][0])
            self.assertEqual('release/v2', branches[1][0])

