import grpc

from .proto import (
    ref_pb2, ref_pb2_grpc,
    commit_pb2, commit_pb2_grpc,
    blob_pb2, blob_pb2_grpc,
    )
from .proto import shared_pb2

GITALY_ADDR = 'unix:/var/opt/gitlab/gitaly/gitaly.socket'

class GitalyClient(object):
    def __init__(self, addr=GITALY_ADDR):
        self.addr = addr
        self._channel = None
        self._refsvc = None
        self._commitsvc = None
        self._blobsvc = None

    def __enter__(self):
        self._channel = grpc.insecure_channel(self.addr)
        self._refsvc = ref_pb2_grpc.RefServiceStub(self._channel)
        self._commitsvc = commit_pb2_grpc.CommitServiceStub(self._channel)
        self._blobsvc = blob_pb2_grpc.BlobServiceStub(self._channel)

        return self

    def __exit__(self, *args):
        self._channel.close()

    def _project_repo(self, project):
        return shared_pb2.Repository(
            storage_name=project.storage,
            relative_path=project.disk_path,
            gl_repository=project.gl_repository,
            )

    def get_branches(self, project):
        repository = self._project_repo(project)
        request = ref_pb2.FindAllBranchesRequest(
            repository=repository
            )

        response = list(self._refsvc.FindAllBranches(request))
        assert len(response) == 1 # Shouldn't this be Unary?

        branches = []
        for branch in response[0].branches:
            ref = (
                branch.name.decode('utf-8').split('/')[-1],
                branch.target.id,
                )
            branches.append(ref)
        assert len(branches) > 0 # Safety check for failed requests

        return branches

    def get_tree_entry(self, project, commit_id, path):
        repository = self._project_repo(project)

        request = commit_pb2.TreeEntryRequest(
            repository=repository,
            revision=commit_id.encode('utf-8'),
            path=path.encode('utf-8'),
            limit = 0,
            )
        response = list(self._commitsvc.TreeEntry(request))
        assert len(response) == 1 # Shouldn't this be Unary?

        entry = response[0]
        return (
            entry.oid,
            entry.size,
            entry.data,
            )
