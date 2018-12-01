# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blob.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import shared_pb2 as shared__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='blob.proto',
  package='gitaly',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nblob.proto\x12\x06gitaly\x1a\x0cshared.proto\"T\n\x0eGetBlobRequest\x12&\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.Repository\x12\x0b\n\x03oid\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x03\":\n\x0fGetBlobResponse\x12\x0c\n\x04size\x18\x01 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0b\n\x03oid\x18\x03 \x01(\t\"\xb6\x01\n\x0fGetBlobsRequest\x12&\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.Repository\x12<\n\x0erevision_paths\x18\x02 \x03(\x0b\x32$.gitaly.GetBlobsRequest.RevisionPath\x12\r\n\x05limit\x18\x03 \x01(\x03\x1a.\n\x0cRevisionPath\x12\x10\n\x08revision\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\x0c\"\x7f\n\x10GetBlobsResponse\x12\x0c\n\x04size\x18\x01 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0b\n\x03oid\x18\x03 \x01(\t\x12\x14\n\x0cis_submodule\x18\x04 \x01(\x08\x12\x0c\n\x04mode\x18\x05 \x01(\x05\x12\x10\n\x08revision\x18\x06 \x01(\t\x12\x0c\n\x04path\x18\x07 \x01(\x0c\"5\n\nLFSPointer\x12\x0c\n\x04size\x18\x01 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0b\n\x03oid\x18\x03 \x01(\t\"8\n\rNewBlobObject\x12\x0c\n\x04size\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\x0c\"Q\n\x15GetLFSPointersRequest\x12&\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.Repository\x12\x10\n\x08\x62lob_ids\x18\x02 \x03(\t\"B\n\x16GetLFSPointersResponse\x12(\n\x0clfs_pointers\x18\x01 \x03(\x0b\x32\x12.gitaly.LFSPointer\"\x8c\x01\n\x18GetNewLFSPointersRequest\x12&\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.Repository\x12\x10\n\x08revision\x18\x02 \x01(\x0c\x12\r\n\x05limit\x18\x03 \x01(\x05\x12\x12\n\nnot_in_all\x18\x04 \x01(\x08\x12\x13\n\x0bnot_in_refs\x18\x05 \x03(\x0c\"E\n\x19GetNewLFSPointersResponse\x12(\n\x0clfs_pointers\x18\x01 \x03(\x0b\x32\x12.gitaly.LFSPointer\"T\n\x18GetAllLFSPointersRequest\x12&\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.Repository\x12\x10\n\x08revision\x18\x02 \x01(\x0c\"E\n\x19GetAllLFSPointersResponse\x12(\n\x0clfs_pointers\x18\x01 \x03(\x0b\x32\x12.gitaly.LFSPointer2\xa1\x03\n\x0b\x42lobService\x12>\n\x07GetBlob\x12\x16.gitaly.GetBlobRequest\x1a\x17.gitaly.GetBlobResponse\"\x00\x30\x01\x12\x41\n\x08GetBlobs\x12\x17.gitaly.GetBlobsRequest\x1a\x18.gitaly.GetBlobsResponse\"\x00\x30\x01\x12S\n\x0eGetLFSPointers\x12\x1d.gitaly.GetLFSPointersRequest\x1a\x1e.gitaly.GetLFSPointersResponse\"\x00\x30\x01\x12\\\n\x11GetNewLFSPointers\x12 .gitaly.GetNewLFSPointersRequest\x1a!.gitaly.GetNewLFSPointersResponse\"\x00\x30\x01\x12\\\n\x11GetAllLFSPointers\x12 .gitaly.GetAllLFSPointersRequest\x1a!.gitaly.GetAllLFSPointersResponse\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[shared__pb2.DESCRIPTOR,])




_GETBLOBREQUEST = _descriptor.Descriptor(
  name='GetBlobRequest',
  full_name='gitaly.GetBlobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository', full_name='gitaly.GetBlobRequest.repository', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oid', full_name='gitaly.GetBlobRequest.oid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='gitaly.GetBlobRequest.limit', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=120,
)


_GETBLOBRESPONSE = _descriptor.Descriptor(
  name='GetBlobResponse',
  full_name='gitaly.GetBlobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='gitaly.GetBlobResponse.size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='gitaly.GetBlobResponse.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oid', full_name='gitaly.GetBlobResponse.oid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=180,
)


_GETBLOBSREQUEST_REVISIONPATH = _descriptor.Descriptor(
  name='RevisionPath',
  full_name='gitaly.GetBlobsRequest.RevisionPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='revision', full_name='gitaly.GetBlobsRequest.RevisionPath.revision', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='gitaly.GetBlobsRequest.RevisionPath.path', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=365,
)

_GETBLOBSREQUEST = _descriptor.Descriptor(
  name='GetBlobsRequest',
  full_name='gitaly.GetBlobsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository', full_name='gitaly.GetBlobsRequest.repository', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revision_paths', full_name='gitaly.GetBlobsRequest.revision_paths', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='gitaly.GetBlobsRequest.limit', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETBLOBSREQUEST_REVISIONPATH, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=183,
  serialized_end=365,
)


_GETBLOBSRESPONSE = _descriptor.Descriptor(
  name='GetBlobsResponse',
  full_name='gitaly.GetBlobsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='gitaly.GetBlobsResponse.size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='gitaly.GetBlobsResponse.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oid', full_name='gitaly.GetBlobsResponse.oid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_submodule', full_name='gitaly.GetBlobsResponse.is_submodule', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='gitaly.GetBlobsResponse.mode', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revision', full_name='gitaly.GetBlobsResponse.revision', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='gitaly.GetBlobsResponse.path', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=494,
)


_LFSPOINTER = _descriptor.Descriptor(
  name='LFSPointer',
  full_name='gitaly.LFSPointer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='gitaly.LFSPointer.size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='gitaly.LFSPointer.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oid', full_name='gitaly.LFSPointer.oid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=496,
  serialized_end=549,
)


_NEWBLOBOBJECT = _descriptor.Descriptor(
  name='NewBlobObject',
  full_name='gitaly.NewBlobObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='gitaly.NewBlobObject.size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oid', full_name='gitaly.NewBlobObject.oid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='gitaly.NewBlobObject.path', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=551,
  serialized_end=607,
)


_GETLFSPOINTERSREQUEST = _descriptor.Descriptor(
  name='GetLFSPointersRequest',
  full_name='gitaly.GetLFSPointersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository', full_name='gitaly.GetLFSPointersRequest.repository', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blob_ids', full_name='gitaly.GetLFSPointersRequest.blob_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=609,
  serialized_end=690,
)


_GETLFSPOINTERSRESPONSE = _descriptor.Descriptor(
  name='GetLFSPointersResponse',
  full_name='gitaly.GetLFSPointersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lfs_pointers', full_name='gitaly.GetLFSPointersResponse.lfs_pointers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=692,
  serialized_end=758,
)


_GETNEWLFSPOINTERSREQUEST = _descriptor.Descriptor(
  name='GetNewLFSPointersRequest',
  full_name='gitaly.GetNewLFSPointersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository', full_name='gitaly.GetNewLFSPointersRequest.repository', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revision', full_name='gitaly.GetNewLFSPointersRequest.revision', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='gitaly.GetNewLFSPointersRequest.limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_in_all', full_name='gitaly.GetNewLFSPointersRequest.not_in_all', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_in_refs', full_name='gitaly.GetNewLFSPointersRequest.not_in_refs', index=4,
      number=5, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=761,
  serialized_end=901,
)


_GETNEWLFSPOINTERSRESPONSE = _descriptor.Descriptor(
  name='GetNewLFSPointersResponse',
  full_name='gitaly.GetNewLFSPointersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lfs_pointers', full_name='gitaly.GetNewLFSPointersResponse.lfs_pointers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=903,
  serialized_end=972,
)


_GETALLLFSPOINTERSREQUEST = _descriptor.Descriptor(
  name='GetAllLFSPointersRequest',
  full_name='gitaly.GetAllLFSPointersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository', full_name='gitaly.GetAllLFSPointersRequest.repository', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revision', full_name='gitaly.GetAllLFSPointersRequest.revision', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=974,
  serialized_end=1058,
)


_GETALLLFSPOINTERSRESPONSE = _descriptor.Descriptor(
  name='GetAllLFSPointersResponse',
  full_name='gitaly.GetAllLFSPointersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lfs_pointers', full_name='gitaly.GetAllLFSPointersResponse.lfs_pointers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1060,
  serialized_end=1129,
)

_GETBLOBREQUEST.fields_by_name['repository'].message_type = shared__pb2._REPOSITORY
_GETBLOBSREQUEST_REVISIONPATH.containing_type = _GETBLOBSREQUEST
_GETBLOBSREQUEST.fields_by_name['repository'].message_type = shared__pb2._REPOSITORY
_GETBLOBSREQUEST.fields_by_name['revision_paths'].message_type = _GETBLOBSREQUEST_REVISIONPATH
_GETLFSPOINTERSREQUEST.fields_by_name['repository'].message_type = shared__pb2._REPOSITORY
_GETLFSPOINTERSRESPONSE.fields_by_name['lfs_pointers'].message_type = _LFSPOINTER
_GETNEWLFSPOINTERSREQUEST.fields_by_name['repository'].message_type = shared__pb2._REPOSITORY
_GETNEWLFSPOINTERSRESPONSE.fields_by_name['lfs_pointers'].message_type = _LFSPOINTER
_GETALLLFSPOINTERSREQUEST.fields_by_name['repository'].message_type = shared__pb2._REPOSITORY
_GETALLLFSPOINTERSRESPONSE.fields_by_name['lfs_pointers'].message_type = _LFSPOINTER
DESCRIPTOR.message_types_by_name['GetBlobRequest'] = _GETBLOBREQUEST
DESCRIPTOR.message_types_by_name['GetBlobResponse'] = _GETBLOBRESPONSE
DESCRIPTOR.message_types_by_name['GetBlobsRequest'] = _GETBLOBSREQUEST
DESCRIPTOR.message_types_by_name['GetBlobsResponse'] = _GETBLOBSRESPONSE
DESCRIPTOR.message_types_by_name['LFSPointer'] = _LFSPOINTER
DESCRIPTOR.message_types_by_name['NewBlobObject'] = _NEWBLOBOBJECT
DESCRIPTOR.message_types_by_name['GetLFSPointersRequest'] = _GETLFSPOINTERSREQUEST
DESCRIPTOR.message_types_by_name['GetLFSPointersResponse'] = _GETLFSPOINTERSRESPONSE
DESCRIPTOR.message_types_by_name['GetNewLFSPointersRequest'] = _GETNEWLFSPOINTERSREQUEST
DESCRIPTOR.message_types_by_name['GetNewLFSPointersResponse'] = _GETNEWLFSPOINTERSRESPONSE
DESCRIPTOR.message_types_by_name['GetAllLFSPointersRequest'] = _GETALLLFSPOINTERSREQUEST
DESCRIPTOR.message_types_by_name['GetAllLFSPointersResponse'] = _GETALLLFSPOINTERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetBlobRequest = _reflection.GeneratedProtocolMessageType('GetBlobRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBLOBREQUEST,
  __module__ = 'blob_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.GetBlobRequest)
  ))
_sym_db.RegisterMessage(GetBlobRequest)

GetBlobResponse = _reflection.GeneratedProtocolMessageType('GetBlobResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETBLOBRESPONSE,
  __module__ = 'blob_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.GetBlobResponse)
  ))
_sym_db.RegisterMessage(GetBlobResponse)

GetBlobsRequest = _reflection.GeneratedProtocolMessageType('GetBlobsRequest', (_message.Message,), dict(

  RevisionPath = _reflection.GeneratedProtocolMessageType('RevisionPath', (_message.Message,), dict(
    DESCRIPTOR = _GETBLOBSREQUEST_REVISIONPATH,
    __module__ = 'blob_pb2'
    # @@protoc_insertion_point(class_scope:gitaly.GetBlobsRequest.RevisionPath)
    ))
  ,
  DESCRIPTOR = _GETBLOBSREQUEST,
  __module__ = 'blob_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.GetBlobsRequest)
  ))
_sym_db.RegisterMessage(GetBlobsRequest)
_sym_db.RegisterMessage(GetBlobsRequest.RevisionPath)

GetBlobsResponse = _reflection.GeneratedProtocolMessageType('GetBlobsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETBLOBSRESPONSE,
  __module__ = 'blob_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.GetBlobsResponse)
  ))
_sym_db.RegisterMessage(GetBlobsResponse)

LFSPointer = _reflection.GeneratedProtocolMessageType('LFSPointer', (_message.Message,), dict(
  DESCRIPTOR = _LFSPOINTER,
  __module__ = 'blob_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.LFSPointer)
  ))
_sym_db.RegisterMessage(LFSPointer)

NewBlobObject = _reflection.GeneratedProtocolMessageType('NewBlobObject', (_message.Message,), dict(
  DESCRIPTOR = _NEWBLOBOBJECT,
  __module__ = 'blob_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.NewBlobObject)
  ))
_sym_db.RegisterMessage(NewBlobObject)

GetLFSPointersRequest = _reflection.GeneratedProtocolMessageType('GetLFSPointersRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETLFSPOINTERSREQUEST,
  __module__ = 'blob_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.GetLFSPointersRequest)
  ))
_sym_db.RegisterMessage(GetLFSPointersRequest)

GetLFSPointersResponse = _reflection.GeneratedProtocolMessageType('GetLFSPointersResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETLFSPOINTERSRESPONSE,
  __module__ = 'blob_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.GetLFSPointersResponse)
  ))
_sym_db.RegisterMessage(GetLFSPointersResponse)

GetNewLFSPointersRequest = _reflection.GeneratedProtocolMessageType('GetNewLFSPointersRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETNEWLFSPOINTERSREQUEST,
  __module__ = 'blob_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.GetNewLFSPointersRequest)
  ))
_sym_db.RegisterMessage(GetNewLFSPointersRequest)

GetNewLFSPointersResponse = _reflection.GeneratedProtocolMessageType('GetNewLFSPointersResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETNEWLFSPOINTERSRESPONSE,
  __module__ = 'blob_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.GetNewLFSPointersResponse)
  ))
_sym_db.RegisterMessage(GetNewLFSPointersResponse)

GetAllLFSPointersRequest = _reflection.GeneratedProtocolMessageType('GetAllLFSPointersRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETALLLFSPOINTERSREQUEST,
  __module__ = 'blob_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.GetAllLFSPointersRequest)
  ))
_sym_db.RegisterMessage(GetAllLFSPointersRequest)

GetAllLFSPointersResponse = _reflection.GeneratedProtocolMessageType('GetAllLFSPointersResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETALLLFSPOINTERSRESPONSE,
  __module__ = 'blob_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.GetAllLFSPointersResponse)
  ))
_sym_db.RegisterMessage(GetAllLFSPointersResponse)



_BLOBSERVICE = _descriptor.ServiceDescriptor(
  name='BlobService',
  full_name='gitaly.BlobService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1132,
  serialized_end=1549,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBlob',
    full_name='gitaly.BlobService.GetBlob',
    index=0,
    containing_service=None,
    input_type=_GETBLOBREQUEST,
    output_type=_GETBLOBRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBlobs',
    full_name='gitaly.BlobService.GetBlobs',
    index=1,
    containing_service=None,
    input_type=_GETBLOBSREQUEST,
    output_type=_GETBLOBSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetLFSPointers',
    full_name='gitaly.BlobService.GetLFSPointers',
    index=2,
    containing_service=None,
    input_type=_GETLFSPOINTERSREQUEST,
    output_type=_GETLFSPOINTERSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetNewLFSPointers',
    full_name='gitaly.BlobService.GetNewLFSPointers',
    index=3,
    containing_service=None,
    input_type=_GETNEWLFSPOINTERSREQUEST,
    output_type=_GETNEWLFSPOINTERSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllLFSPointers',
    full_name='gitaly.BlobService.GetAllLFSPointers',
    index=4,
    containing_service=None,
    input_type=_GETALLLFSPOINTERSREQUEST,
    output_type=_GETALLLFSPOINTERSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BLOBSERVICE)

DESCRIPTOR.services_by_name['BlobService'] = _BLOBSERVICE

# @@protoc_insertion_point(module_scope)