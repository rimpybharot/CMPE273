# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: encoder.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='encoder.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rencoder.proto\"\x1c\n\rEncodeRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x1c\n\x0e\x45ncodeResponse\x12\n\n\x02id\x18\x01 \x01(\r\"\x1b\n\rDecodeRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x1d\n\x0e\x44\x65\x63odeResponse\x12\x0b\n\x03url\x18\x01 \x01(\t2c\n\x07\x45ncoder\x12+\n\x06\x65ncode\x12\x0e.EncodeRequest\x1a\x0f.EncodeResponse\"\x00\x12+\n\x06\x64\x65\x63ode\x12\x0e.DecodeRequest\x1a\x0f.DecodeResponse\"\x00\x62\x06proto3')
)




_ENCODEREQUEST = _descriptor.Descriptor(
  name='EncodeRequest',
  full_name='EncodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='EncodeRequest.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=45,
)


_ENCODERESPONSE = _descriptor.Descriptor(
  name='EncodeResponse',
  full_name='EncodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='EncodeResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=75,
)


_DECODEREQUEST = _descriptor.Descriptor(
  name='DecodeRequest',
  full_name='DecodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='DecodeRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=104,
)


_DECODERESPONSE = _descriptor.Descriptor(
  name='DecodeResponse',
  full_name='DecodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='DecodeResponse.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=135,
)

DESCRIPTOR.message_types_by_name['EncodeRequest'] = _ENCODEREQUEST
DESCRIPTOR.message_types_by_name['EncodeResponse'] = _ENCODERESPONSE
DESCRIPTOR.message_types_by_name['DecodeRequest'] = _DECODEREQUEST
DESCRIPTOR.message_types_by_name['DecodeResponse'] = _DECODERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EncodeRequest = _reflection.GeneratedProtocolMessageType('EncodeRequest', (_message.Message,), dict(
  DESCRIPTOR = _ENCODEREQUEST,
  __module__ = 'encoder_pb2'
  # @@protoc_insertion_point(class_scope:EncodeRequest)
  ))
_sym_db.RegisterMessage(EncodeRequest)

EncodeResponse = _reflection.GeneratedProtocolMessageType('EncodeResponse', (_message.Message,), dict(
  DESCRIPTOR = _ENCODERESPONSE,
  __module__ = 'encoder_pb2'
  # @@protoc_insertion_point(class_scope:EncodeResponse)
  ))
_sym_db.RegisterMessage(EncodeResponse)

DecodeRequest = _reflection.GeneratedProtocolMessageType('DecodeRequest', (_message.Message,), dict(
  DESCRIPTOR = _DECODEREQUEST,
  __module__ = 'encoder_pb2'
  # @@protoc_insertion_point(class_scope:DecodeRequest)
  ))
_sym_db.RegisterMessage(DecodeRequest)

DecodeResponse = _reflection.GeneratedProtocolMessageType('DecodeResponse', (_message.Message,), dict(
  DESCRIPTOR = _DECODERESPONSE,
  __module__ = 'encoder_pb2'
  # @@protoc_insertion_point(class_scope:DecodeResponse)
  ))
_sym_db.RegisterMessage(DecodeResponse)



_ENCODER = _descriptor.ServiceDescriptor(
  name='Encoder',
  full_name='Encoder',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=137,
  serialized_end=236,
  methods=[
  _descriptor.MethodDescriptor(
    name='encode',
    full_name='Encoder.encode',
    index=0,
    containing_service=None,
    input_type=_ENCODEREQUEST,
    output_type=_ENCODERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='decode',
    full_name='Encoder.decode',
    index=1,
    containing_service=None,
    input_type=_DECODEREQUEST,
    output_type=_DECODERESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENCODER)

DESCRIPTOR.services_by_name['Encoder'] = _ENCODER

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class EncoderStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.encode = channel.unary_unary(
          '/Encoder/encode',
          request_serializer=EncodeRequest.SerializeToString,
          response_deserializer=EncodeResponse.FromString,
          )
      self.decode = channel.unary_unary(
          '/Encoder/decode',
          request_serializer=DecodeRequest.SerializeToString,
          response_deserializer=DecodeResponse.FromString,
          )


  class EncoderServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def encode(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def decode(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_EncoderServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'encode': grpc.unary_unary_rpc_method_handler(
            servicer.encode,
            request_deserializer=EncodeRequest.FromString,
            response_serializer=EncodeResponse.SerializeToString,
        ),
        'decode': grpc.unary_unary_rpc_method_handler(
            servicer.decode,
            request_deserializer=DecodeRequest.FromString,
            response_serializer=DecodeResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Encoder', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaEncoderServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def encode(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def decode(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaEncoderStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def encode(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    encode.future = None
    def decode(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    decode.future = None


  def beta_create_Encoder_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Encoder', 'decode'): DecodeRequest.FromString,
      ('Encoder', 'encode'): EncodeRequest.FromString,
    }
    response_serializers = {
      ('Encoder', 'decode'): DecodeResponse.SerializeToString,
      ('Encoder', 'encode'): EncodeResponse.SerializeToString,
    }
    method_implementations = {
      ('Encoder', 'decode'): face_utilities.unary_unary_inline(servicer.decode),
      ('Encoder', 'encode'): face_utilities.unary_unary_inline(servicer.encode),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Encoder_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Encoder', 'decode'): DecodeRequest.SerializeToString,
      ('Encoder', 'encode'): EncodeRequest.SerializeToString,
    }
    response_deserializers = {
      ('Encoder', 'decode'): DecodeResponse.FromString,
      ('Encoder', 'encode'): EncodeResponse.FromString,
    }
    cardinalities = {
      'decode': cardinality.Cardinality.UNARY_UNARY,
      'encode': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Encoder', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
