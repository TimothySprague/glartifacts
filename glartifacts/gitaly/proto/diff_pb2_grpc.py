# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import diff_pb2 as diff__pb2


class DiffServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CommitDiff = channel.unary_stream(
        '/gitaly.DiffService/CommitDiff',
        request_serializer=diff__pb2.CommitDiffRequest.SerializeToString,
        response_deserializer=diff__pb2.CommitDiffResponse.FromString,
        )
    self.CommitDelta = channel.unary_stream(
        '/gitaly.DiffService/CommitDelta',
        request_serializer=diff__pb2.CommitDeltaRequest.SerializeToString,
        response_deserializer=diff__pb2.CommitDeltaResponse.FromString,
        )
    self.CommitPatch = channel.unary_stream(
        '/gitaly.DiffService/CommitPatch',
        request_serializer=diff__pb2.CommitPatchRequest.SerializeToString,
        response_deserializer=diff__pb2.CommitPatchResponse.FromString,
        )
    self.RawDiff = channel.unary_stream(
        '/gitaly.DiffService/RawDiff',
        request_serializer=diff__pb2.RawDiffRequest.SerializeToString,
        response_deserializer=diff__pb2.RawDiffResponse.FromString,
        )
    self.RawPatch = channel.unary_stream(
        '/gitaly.DiffService/RawPatch',
        request_serializer=diff__pb2.RawPatchRequest.SerializeToString,
        response_deserializer=diff__pb2.RawPatchResponse.FromString,
        )
    self.DiffStats = channel.unary_stream(
        '/gitaly.DiffService/DiffStats',
        request_serializer=diff__pb2.DiffStatsRequest.SerializeToString,
        response_deserializer=diff__pb2.DiffStatsResponse.FromString,
        )


class DiffServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CommitDiff(self, request, context):
    """Returns stream of CommitDiffResponse with patches chunked over messages
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CommitDelta(self, request, context):
    """Return a stream so we can divide the response in chunks of deltas
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CommitPatch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RawDiff(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RawPatch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DiffStats(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DiffServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CommitDiff': grpc.unary_stream_rpc_method_handler(
          servicer.CommitDiff,
          request_deserializer=diff__pb2.CommitDiffRequest.FromString,
          response_serializer=diff__pb2.CommitDiffResponse.SerializeToString,
      ),
      'CommitDelta': grpc.unary_stream_rpc_method_handler(
          servicer.CommitDelta,
          request_deserializer=diff__pb2.CommitDeltaRequest.FromString,
          response_serializer=diff__pb2.CommitDeltaResponse.SerializeToString,
      ),
      'CommitPatch': grpc.unary_stream_rpc_method_handler(
          servicer.CommitPatch,
          request_deserializer=diff__pb2.CommitPatchRequest.FromString,
          response_serializer=diff__pb2.CommitPatchResponse.SerializeToString,
      ),
      'RawDiff': grpc.unary_stream_rpc_method_handler(
          servicer.RawDiff,
          request_deserializer=diff__pb2.RawDiffRequest.FromString,
          response_serializer=diff__pb2.RawDiffResponse.SerializeToString,
      ),
      'RawPatch': grpc.unary_stream_rpc_method_handler(
          servicer.RawPatch,
          request_deserializer=diff__pb2.RawPatchRequest.FromString,
          response_serializer=diff__pb2.RawPatchResponse.SerializeToString,
      ),
      'DiffStats': grpc.unary_stream_rpc_method_handler(
          servicer.DiffStats,
          request_deserializer=diff__pb2.DiffStatsRequest.FromString,
          response_serializer=diff__pb2.DiffStatsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gitaly.DiffService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))