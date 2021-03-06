# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import server_pb2 as server__pb2


class ServerServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ServerInfo = channel.unary_unary(
        '/gitaly.ServerService/ServerInfo',
        request_serializer=server__pb2.ServerInfoRequest.SerializeToString,
        response_deserializer=server__pb2.ServerInfoResponse.FromString,
        )


class ServerServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ServerInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ServerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ServerInfo': grpc.unary_unary_rpc_method_handler(
          servicer.ServerInfo,
          request_deserializer=server__pb2.ServerInfoRequest.FromString,
          response_serializer=server__pb2.ServerInfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gitaly.ServerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
