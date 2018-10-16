# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import notifications_pb2 as notifications__pb2


class NotificationServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PostReceive = channel.unary_unary(
        '/gitaly.NotificationService/PostReceive',
        request_serializer=notifications__pb2.PostReceiveRequest.SerializeToString,
        response_deserializer=notifications__pb2.PostReceiveResponse.FromString,
        )


class NotificationServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def PostReceive(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NotificationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PostReceive': grpc.unary_unary_rpc_method_handler(
          servicer.PostReceive,
          request_deserializer=notifications__pb2.PostReceiveRequest.FromString,
          response_serializer=notifications__pb2.PostReceiveResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gitaly.NotificationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
