# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import remote_pb2 as remote__pb2


class RemoteServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddRemote = channel.unary_unary(
        '/gitaly.RemoteService/AddRemote',
        request_serializer=remote__pb2.AddRemoteRequest.SerializeToString,
        response_deserializer=remote__pb2.AddRemoteResponse.FromString,
        )
    self.FetchInternalRemote = channel.unary_unary(
        '/gitaly.RemoteService/FetchInternalRemote',
        request_serializer=remote__pb2.FetchInternalRemoteRequest.SerializeToString,
        response_deserializer=remote__pb2.FetchInternalRemoteResponse.FromString,
        )
    self.RemoveRemote = channel.unary_unary(
        '/gitaly.RemoteService/RemoveRemote',
        request_serializer=remote__pb2.RemoveRemoteRequest.SerializeToString,
        response_deserializer=remote__pb2.RemoveRemoteResponse.FromString,
        )
    self.UpdateRemoteMirror = channel.stream_unary(
        '/gitaly.RemoteService/UpdateRemoteMirror',
        request_serializer=remote__pb2.UpdateRemoteMirrorRequest.SerializeToString,
        response_deserializer=remote__pb2.UpdateRemoteMirrorResponse.FromString,
        )
    self.FindRemoteRepository = channel.unary_unary(
        '/gitaly.RemoteService/FindRemoteRepository',
        request_serializer=remote__pb2.FindRemoteRepositoryRequest.SerializeToString,
        response_deserializer=remote__pb2.FindRemoteRepositoryResponse.FromString,
        )
    self.FindRemoteRootRef = channel.unary_unary(
        '/gitaly.RemoteService/FindRemoteRootRef',
        request_serializer=remote__pb2.FindRemoteRootRefRequest.SerializeToString,
        response_deserializer=remote__pb2.FindRemoteRootRefResponse.FromString,
        )


class RemoteServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def AddRemote(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchInternalRemote(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveRemote(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateRemoteMirror(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindRemoteRepository(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindRemoteRootRef(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RemoteServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddRemote': grpc.unary_unary_rpc_method_handler(
          servicer.AddRemote,
          request_deserializer=remote__pb2.AddRemoteRequest.FromString,
          response_serializer=remote__pb2.AddRemoteResponse.SerializeToString,
      ),
      'FetchInternalRemote': grpc.unary_unary_rpc_method_handler(
          servicer.FetchInternalRemote,
          request_deserializer=remote__pb2.FetchInternalRemoteRequest.FromString,
          response_serializer=remote__pb2.FetchInternalRemoteResponse.SerializeToString,
      ),
      'RemoveRemote': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveRemote,
          request_deserializer=remote__pb2.RemoveRemoteRequest.FromString,
          response_serializer=remote__pb2.RemoveRemoteResponse.SerializeToString,
      ),
      'UpdateRemoteMirror': grpc.stream_unary_rpc_method_handler(
          servicer.UpdateRemoteMirror,
          request_deserializer=remote__pb2.UpdateRemoteMirrorRequest.FromString,
          response_serializer=remote__pb2.UpdateRemoteMirrorResponse.SerializeToString,
      ),
      'FindRemoteRepository': grpc.unary_unary_rpc_method_handler(
          servicer.FindRemoteRepository,
          request_deserializer=remote__pb2.FindRemoteRepositoryRequest.FromString,
          response_serializer=remote__pb2.FindRemoteRepositoryResponse.SerializeToString,
      ),
      'FindRemoteRootRef': grpc.unary_unary_rpc_method_handler(
          servicer.FindRemoteRootRef,
          request_deserializer=remote__pb2.FindRemoteRootRefRequest.FromString,
          response_serializer=remote__pb2.FindRemoteRootRefResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gitaly.RemoteService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
