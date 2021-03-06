# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import blob_pb2 as blob__pb2


class BlobServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetBlob = channel.unary_stream(
        '/gitaly.BlobService/GetBlob',
        request_serializer=blob__pb2.GetBlobRequest.SerializeToString,
        response_deserializer=blob__pb2.GetBlobResponse.FromString,
        )
    self.GetBlobs = channel.unary_stream(
        '/gitaly.BlobService/GetBlobs',
        request_serializer=blob__pb2.GetBlobsRequest.SerializeToString,
        response_deserializer=blob__pb2.GetBlobsResponse.FromString,
        )
    self.GetLFSPointers = channel.unary_stream(
        '/gitaly.BlobService/GetLFSPointers',
        request_serializer=blob__pb2.GetLFSPointersRequest.SerializeToString,
        response_deserializer=blob__pb2.GetLFSPointersResponse.FromString,
        )
    self.GetNewLFSPointers = channel.unary_stream(
        '/gitaly.BlobService/GetNewLFSPointers',
        request_serializer=blob__pb2.GetNewLFSPointersRequest.SerializeToString,
        response_deserializer=blob__pb2.GetNewLFSPointersResponse.FromString,
        )
    self.GetAllLFSPointers = channel.unary_stream(
        '/gitaly.BlobService/GetAllLFSPointers',
        request_serializer=blob__pb2.GetAllLFSPointersRequest.SerializeToString,
        response_deserializer=blob__pb2.GetAllLFSPointersResponse.FromString,
        )


class BlobServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetBlob(self, request, context):
    """GetBlob returns the contents of a blob object referenced by its object
    ID. We use a stream to return a chunked arbitrarily large binary
    response
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBlobs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLFSPointers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNewLFSPointers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllLFSPointers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BlobServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetBlob': grpc.unary_stream_rpc_method_handler(
          servicer.GetBlob,
          request_deserializer=blob__pb2.GetBlobRequest.FromString,
          response_serializer=blob__pb2.GetBlobResponse.SerializeToString,
      ),
      'GetBlobs': grpc.unary_stream_rpc_method_handler(
          servicer.GetBlobs,
          request_deserializer=blob__pb2.GetBlobsRequest.FromString,
          response_serializer=blob__pb2.GetBlobsResponse.SerializeToString,
      ),
      'GetLFSPointers': grpc.unary_stream_rpc_method_handler(
          servicer.GetLFSPointers,
          request_deserializer=blob__pb2.GetLFSPointersRequest.FromString,
          response_serializer=blob__pb2.GetLFSPointersResponse.SerializeToString,
      ),
      'GetNewLFSPointers': grpc.unary_stream_rpc_method_handler(
          servicer.GetNewLFSPointers,
          request_deserializer=blob__pb2.GetNewLFSPointersRequest.FromString,
          response_serializer=blob__pb2.GetNewLFSPointersResponse.SerializeToString,
      ),
      'GetAllLFSPointers': grpc.unary_stream_rpc_method_handler(
          servicer.GetAllLFSPointers,
          request_deserializer=blob__pb2.GetAllLFSPointersRequest.FromString,
          response_serializer=blob__pb2.GetAllLFSPointersResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gitaly.BlobService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
