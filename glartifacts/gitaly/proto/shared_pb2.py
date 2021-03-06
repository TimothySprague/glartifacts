# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shared.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='shared.proto',
  package='gitaly',
  syntax='proto3',
  serialized_options=_b('Z\010gitalypb'),
  serialized_pb=_b('\n\x0cshared.proto\x12\x06gitaly\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa4\x01\n\nRepository\x12\x14\n\x0cstorage_name\x18\x02 \x01(\t\x12\x15\n\rrelative_path\x18\x03 \x01(\t\x12\x1c\n\x14git_object_directory\x18\x04 \x01(\t\x12(\n git_alternate_object_directories\x18\x05 \x03(\t\x12\x15\n\rgl_repository\x18\x06 \x01(\tJ\x04\x08\x01\x10\x02R\x04path\"\xac\x01\n\tGitCommit\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07subject\x18\x02 \x01(\x0c\x12\x0c\n\x04\x62ody\x18\x03 \x01(\x0c\x12$\n\x06\x61uthor\x18\x04 \x01(\x0b\x32\x14.gitaly.CommitAuthor\x12\'\n\tcommitter\x18\x05 \x01(\x0b\x32\x14.gitaly.CommitAuthor\x12\x12\n\nparent_ids\x18\x06 \x03(\t\x12\x11\n\tbody_size\x18\x07 \x01(\x03\"U\n\x0c\x43ommitAuthor\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\r\n\x05\x65mail\x18\x02 \x01(\x0c\x12(\n\x04\x64\x61te\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x1b\n\nExitStatus\x12\r\n\x05value\x18\x01 \x01(\x05\"@\n\x06\x42ranch\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12(\n\rtarget_commit\x18\x02 \x01(\x0b\x32\x11.gitaly.GitCommit\"\x96\x01\n\x03Tag\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\n\n\x02id\x18\x02 \x01(\t\x12(\n\rtarget_commit\x18\x03 \x01(\x0b\x32\x11.gitaly.GitCommit\x12\x0f\n\x07message\x18\x04 \x01(\x0c\x12\x14\n\x0cmessage_size\x18\x05 \x01(\x03\x12$\n\x06tagger\x18\x06 \x01(\x0b\x32\x14.gitaly.CommitAuthor\"G\n\x04User\x12\r\n\x05gl_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\x0c\x12\r\n\x05\x65mail\x18\x03 \x01(\x0c\x12\x13\n\x0bgl_username\x18\x04 \x01(\tB\nZ\x08gitalypbb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_REPOSITORY = _descriptor.Descriptor(
  name='Repository',
  full_name='gitaly.Repository',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='storage_name', full_name='gitaly.Repository.storage_name', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relative_path', full_name='gitaly.Repository.relative_path', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='git_object_directory', full_name='gitaly.Repository.git_object_directory', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='git_alternate_object_directories', full_name='gitaly.Repository.git_alternate_object_directories', index=3,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gl_repository', full_name='gitaly.Repository.gl_repository', index=4,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=58,
  serialized_end=222,
)


_GITCOMMIT = _descriptor.Descriptor(
  name='GitCommit',
  full_name='gitaly.GitCommit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gitaly.GitCommit.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subject', full_name='gitaly.GitCommit.subject', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='gitaly.GitCommit.body', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='gitaly.GitCommit.author', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='committer', full_name='gitaly.GitCommit.committer', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_ids', full_name='gitaly.GitCommit.parent_ids', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body_size', full_name='gitaly.GitCommit.body_size', index=6,
      number=7, type=3, cpp_type=2, label=1,
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
  serialized_start=225,
  serialized_end=397,
)


_COMMITAUTHOR = _descriptor.Descriptor(
  name='CommitAuthor',
  full_name='gitaly.CommitAuthor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gitaly.CommitAuthor.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='gitaly.CommitAuthor.email', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='gitaly.CommitAuthor.date', index=2,
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
  serialized_start=399,
  serialized_end=484,
)


_EXITSTATUS = _descriptor.Descriptor(
  name='ExitStatus',
  full_name='gitaly.ExitStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='gitaly.ExitStatus.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=486,
  serialized_end=513,
)


_BRANCH = _descriptor.Descriptor(
  name='Branch',
  full_name='gitaly.Branch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gitaly.Branch.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_commit', full_name='gitaly.Branch.target_commit', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=515,
  serialized_end=579,
)


_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='gitaly.Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gitaly.Tag.name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='gitaly.Tag.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_commit', full_name='gitaly.Tag.target_commit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='gitaly.Tag.message', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_size', full_name='gitaly.Tag.message_size', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagger', full_name='gitaly.Tag.tagger', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=582,
  serialized_end=732,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='gitaly.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gl_id', full_name='gitaly.User.gl_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='gitaly.User.name', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='gitaly.User.email', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gl_username', full_name='gitaly.User.gl_username', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=734,
  serialized_end=805,
)

_GITCOMMIT.fields_by_name['author'].message_type = _COMMITAUTHOR
_GITCOMMIT.fields_by_name['committer'].message_type = _COMMITAUTHOR
_COMMITAUTHOR.fields_by_name['date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BRANCH.fields_by_name['target_commit'].message_type = _GITCOMMIT
_TAG.fields_by_name['target_commit'].message_type = _GITCOMMIT
_TAG.fields_by_name['tagger'].message_type = _COMMITAUTHOR
DESCRIPTOR.message_types_by_name['Repository'] = _REPOSITORY
DESCRIPTOR.message_types_by_name['GitCommit'] = _GITCOMMIT
DESCRIPTOR.message_types_by_name['CommitAuthor'] = _COMMITAUTHOR
DESCRIPTOR.message_types_by_name['ExitStatus'] = _EXITSTATUS
DESCRIPTOR.message_types_by_name['Branch'] = _BRANCH
DESCRIPTOR.message_types_by_name['Tag'] = _TAG
DESCRIPTOR.message_types_by_name['User'] = _USER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Repository = _reflection.GeneratedProtocolMessageType('Repository', (_message.Message,), dict(
  DESCRIPTOR = _REPOSITORY,
  __module__ = 'shared_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.Repository)
  ))
_sym_db.RegisterMessage(Repository)

GitCommit = _reflection.GeneratedProtocolMessageType('GitCommit', (_message.Message,), dict(
  DESCRIPTOR = _GITCOMMIT,
  __module__ = 'shared_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.GitCommit)
  ))
_sym_db.RegisterMessage(GitCommit)

CommitAuthor = _reflection.GeneratedProtocolMessageType('CommitAuthor', (_message.Message,), dict(
  DESCRIPTOR = _COMMITAUTHOR,
  __module__ = 'shared_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.CommitAuthor)
  ))
_sym_db.RegisterMessage(CommitAuthor)

ExitStatus = _reflection.GeneratedProtocolMessageType('ExitStatus', (_message.Message,), dict(
  DESCRIPTOR = _EXITSTATUS,
  __module__ = 'shared_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.ExitStatus)
  ))
_sym_db.RegisterMessage(ExitStatus)

Branch = _reflection.GeneratedProtocolMessageType('Branch', (_message.Message,), dict(
  DESCRIPTOR = _BRANCH,
  __module__ = 'shared_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.Branch)
  ))
_sym_db.RegisterMessage(Branch)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), dict(
  DESCRIPTOR = _TAG,
  __module__ = 'shared_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.Tag)
  ))
_sym_db.RegisterMessage(Tag)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'shared_pb2'
  # @@protoc_insertion_point(class_scope:gitaly.User)
  ))
_sym_db.RegisterMessage(User)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
