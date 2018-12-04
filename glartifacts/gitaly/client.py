import grpc

from .proto import ref_pb2, ref_pb2_grpc
from .proto import shared_pb2

GITALY_ADDR = 'unix:/var/opt/gitlab/gitaly/gitaly.socket'

class GitalyClient(object):
    def __init__(self, addr=GITALY_ADDR):
        self.addr = addr
        self._channel = None
        self._ref_service = None

    def __enter__(self):
        self._channel = grpc.insecure_channel(self.addr)
        self._ref_service = ref_pb2_grpc.RefServiceStub(self._channel)

        return self

    def __exit__(self, *args):
        self._channel.close()

    def get_branches(self, project):
        repository = shared_pb2.Repository(
            storage_name=project.storage,
            relative_path=project.disk_path,
            gl_repository=project.gl_repository,
            )
        request = ref_pb2.FindAllBranchesRequest(
            repository=repository
            )

        response = list(self._ref_service.FindAllBranches(request))
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
