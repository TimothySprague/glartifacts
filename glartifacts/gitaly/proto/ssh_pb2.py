# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ssh.proto

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
  name='ssh.proto',
  package='gitaly',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tssh.proto\x12\x06gitaly\x1a\x0cshared.proto\"\x9c\x01\n\x14SSHUploadPackRequest\x12&\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.Repository\x12\r\n\x05stdin\x18\x02 \x01(\x0c\x12\x1a\n\x12git_config_options\x18\x04 \x03(\t\x12\x14\n\x0cgit_protocol\x18\x05 \x01(\tJ\x04\x08\x03\x10\x04R\x15git_config_parameters\"`\n\x15SSHUploadPackResponse\x12\x0e\n\x06stdout\x18\x01 \x01(\x0c\x12\x0e\n\x06stderr\x18\x02 \x01(\x0c\x12\'\n\x0b\x65xit_status\x18\x03 \x01(\x0b\x32\x12.gitaly.ExitStatus\"\xbb\x01\n\x15SSHReceivePackRequest\x12&\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.Repository\x12\r\n\x05stdin\x18\x02 \x01(\x0c\x12\r\n\x05gl_id\x18\x03 \x01(\t\x12\x15\n\rgl_repository\x18\x04 \x01(\t\x12\x13\n\x0bgl_username\x18\x05 \x01(\t\x12\x14\n\x0cgit_protocol\x18\x06 \x01(\t\x12\x1a\n\x12git_config_options\x18\x07 \x03(\t\"a\n\x16SSHReceivePackResponse\x12\x0e\n\x06stdout\x18\x01 \x01(\x0c\x12\x0e\n\x06stderr\x18\x02 \x01(\x0c\x12\'\n\x0b\x65xit_status\x18\x03 \x01(\x0b\x32\x12.gitaly.ExitStatus\"P\n\x17SSHUploadArchiveRequest\x12&\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.Repository\x12\r\n\x05stdin\x18\x02 \x01(\x0c\"c\n\x18SSHUploadArchiveResponse\x12\x0e\n\x06stdout\x18\x01 \x01(\x0c\x12\x0e\n\x06stderr\x18\x02 \x01(\x0c\x12\'\n\x0b\x65xit_status\x18\x03 \x01(\x0b\x32\x12.gitaly.ExitStatus2\x94\x02\n\nSSHService\x12R\n\rSSHUploadPack\x12\x1c.gitaly.SSHUploadPackRequest\x1a\x1d.gitaly.SSHUploadPackResponse\"\x00(\x01\x30\x01\x12U\n\x0eSSHReceivePack\x12\x1d.gitaly.SSHReceivePackRequest\x1a\x1e.gitaly.SSHReceivePackResponse\"\x00(\x01\x30\x01\x12[\n\x10SSHUploadArchive\x12\x1f.gitaly.SSHUploadArchiveRequest\x1a .gitaly.SSHUploadArchiveResponse\"\x00(\x01\x30\x01\x62\x06proto3')
  ,
  dependencies=[shared__pb2.DESCRIPTOR,])




_SSHUPLOADPACKREQUEST = _descriptor.Descriptor(
  name='SSHUploadPackRequest',
  full_name='gitaly.SSHUploadPackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository', full_name='gitaly.SSHUploadPackRequest.repository', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stdin', full_name='gitaly.SSHUploadPackRequest.stdin', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='git_config_options', full_name='gitaly.SSHUploadPackRequest.git_config_options', index=2,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='git_protocol', full_name='gitaly.SSHUploadPackRequest.git_protocol', index=3,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=36,
  serialized_end=192,
)


_SSHUPLOADPACKRESPONSE = _descriptor.Descriptor(
  name='SSHUploadPackResponse',
  full_name='gitaly.SSHUploadPackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stdout', full_name='gitaly.SSHUploadPackResponse.stdout', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stderr', full_name='gitaly.SSHUploadPackResponse.stderr', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit_status', full_name='gitaly.SSHUploadPackResponse.exit_status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=194,
  serialized_end=290,
)


_SSHRECEIVEPACKREQUEST = _descriptor.Descriptor(
  name='SSHReceivePackRequest',
  full_name='gitaly.SSHReceivePackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository', full_name='gitaly.SSHReceivePackRequest.repository', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stdin', full_name='gitaly.SSHReceivePackRequest.stdin', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gl_id', full_name='gitaly.SSHReceivePackRequest.gl_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gl_repository', full_name='gitaly.SSHReceivePackRequest.gl_repository', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gl_username', full_name='gitaly.SSHReceivePackRequest.gl_username', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='git_protocol', full_name='gitaly.SSHReceivePackRequest.git_protocol', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='git_config_options', full_name='gitaly.SSHReceivePackRequest.git_config_options', index=6,
      number=7, type=9, cpp_type=9, label=3,
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
  serialized_start=293,
  serialized_end=480,
)


_SSHRECEIVEPACKRESPONSE = _descriptor.Descriptor(
  name='SSHReceivePackResponse',
  full_name='gitaly.SSHReceivePackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stdout', full_name='gitaly.SSHReceivePackResponse.stdout', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stderr', full_name='gitaly.SSHReceivePackResponse.stderr', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit_status', full_name='gitaly.SSHReceivePackResponse.exit_status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=482,
  serialized_end=579,
)


_SSHUPLOADARCHIVEREQUEST = _descriptor.Descriptor(
  name='SSHUploadArchiveRequest',
  full_name='gitaly.SSHUploadArchiveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository', full_name='gitaly.SSHUploadArchiveRequest.repository', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stdin', full_name='gitaly.SSHUploadArchiveRequest.stdin', index=1,
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
  serialized_start=581,
  serialized_end=661,
)


_SSHUPLOADARCHIVERESPONSE = _descriptor.Descriptor(
  name='SSHUploadArchiveResponse',
  full_name='gitaly.SSHUploadArchiveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stdout', full_name='gitaly.SSHUploadArchiveResponse.stdout', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stderr', full_name='gitaly.SSHUploadArchiveResponse.stderr', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit_status', full_name='gitaly.SSHUploadArchiveResponse.exit_status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=663,
  serialized_end=762,
)

_SSHUPLOADPACKREQUEST.fields_by_name['repository'].message_type = shared__pb2._REPOSITORY
_SSHUPLOADPACKRESPONSE.fields_by_name['exit_status'].message_type = shared__pb2._EXITSTATUS
_SSHRECEIVEPACKREQUEST.fields_by_name['repository'].message_type = shared__pb2._REPOSITORY
_SSHRECEIVEPACKRESPONSE.fields_by_name['exit_status'].message_type = shared__pb2._EXITSTATUS
_SSHUPLOADARCHIVEREQUEST.fields_by_name['repository'].message_type = shared__pb2._REPOSITORY
_SSHUPLOADARCHIVERESPONSE.fields_by_name['exit_status'].message_type = shared__pb2._EXITSTATUS
DESCRIPTOR.message_types_by_name['SSHUploadPackRequest'] = _SSHUPLOADPACKREQUEST
DESCRIPTOR.message_types_by_name['SSHUploadPackResponse'] = _SSHUPLOADPACKRESPONSE
DESCRIPTOR.message_types_by_name['SSHReceivePackRequest'] = _SSHRECEIVEPACKREQUEST
DESCRIPTOR.message_types_by_name['SSHReceivePackResponse'] = _SSHRECEIVEPACKRESPONSE
DESCRIPTOR.message_types_by_name['SSHUploadArchiveRequest'] = _SSHUPLOADARCHIVEREQUEST
DESCRIPTOR.message_types_by_name['SSHUploadArchiveResponse'] = _SSHUPLOADARCHIVERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SSHUploadPackRequest = _reflection.GeneratedProtocolMessageType('SSHUploadPackRequest', (_message.Message,), dict(
  DESCRIPTOR = _SSHUPLOADPACKREQUEST,
  __module__ = 'ssh_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.SSHUploadPackRequest)
  ))
_sym_db.RegisterMessage(SSHUploadPackRequest)

SSHUploadPackResponse = _reflection.GeneratedProtocolMessageType('SSHUploadPackResponse', (_message.Message,), dict(
  DESCRIPTOR = _SSHUPLOADPACKRESPONSE,
  __module__ = 'ssh_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.SSHUploadPackResponse)
  ))
_sym_db.RegisterMessage(SSHUploadPackResponse)

SSHReceivePackRequest = _reflection.GeneratedProtocolMessageType('SSHReceivePackRequest', (_message.Message,), dict(
  DESCRIPTOR = _SSHRECEIVEPACKREQUEST,
  __module__ = 'ssh_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.SSHReceivePackRequest)
  ))
_sym_db.RegisterMessage(SSHReceivePackRequest)

SSHReceivePackResponse = _reflection.GeneratedProtocolMessageType('SSHReceivePackResponse', (_message.Message,), dict(
  DESCRIPTOR = _SSHRECEIVEPACKRESPONSE,
  __module__ = 'ssh_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.SSHReceivePackResponse)
  ))
_sym_db.RegisterMessage(SSHReceivePackResponse)

SSHUploadArchiveRequest = _reflection.GeneratedProtocolMessageType('SSHUploadArchiveRequest', (_message.Message,), dict(
  DESCRIPTOR = _SSHUPLOADARCHIVEREQUEST,
  __module__ = 'ssh_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.SSHUploadArchiveRequest)
  ))
_sym_db.RegisterMessage(SSHUploadArchiveRequest)

SSHUploadArchiveResponse = _reflection.GeneratedProtocolMessageType('SSHUploadArchiveResponse', (_message.Message,), dict(
  DESCRIPTOR = _SSHUPLOADARCHIVERESPONSE,
  __module__ = 'ssh_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.SSHUploadArchiveResponse)
  ))
_sym_db.RegisterMessage(SSHUploadArchiveResponse)



_SSHSERVICE = _descriptor.ServiceDescriptor(
  name='SSHService',
  full_name='gitaly.SSHService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=765,
  serialized_end=1041,
  methods=[
  _descriptor.MethodDescriptor(
    name='SSHUploadPack',
    full_name='gitaly.SSHService.SSHUploadPack',
    index=0,
    containing_service=None,
    input_type=_SSHUPLOADPACKREQUEST,
    output_type=_SSHUPLOADPACKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SSHReceivePack',
    full_name='gitaly.SSHService.SSHReceivePack',
    index=1,
    containing_service=None,
    input_type=_SSHRECEIVEPACKREQUEST,
    output_type=_SSHRECEIVEPACKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SSHUploadArchive',
    full_name='gitaly.SSHService.SSHUploadArchive',
    index=2,
    containing_service=None,
    input_type=_SSHUPLOADARCHIVEREQUEST,
    output_type=_SSHUPLOADARCHIVERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SSHSERVICE)

DESCRIPTOR.services_by_name['SSHService'] = _SSHSERVICE

# @@protoc_insertion_point(module_scope)