# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import bitkey_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='wallet.proto',
  package='',
  serialized_pb='\n\x0cwallet.proto\x1a\x0c\x62itkey.proto\"a\n\x06Wallet\x12\x18\n\x04\x61lgo\x18\x01 \x02(\x0e\x32\n.Algorithm\x12\x0e\n\x06secexp\x18\x02 \x02(\x0c\x12\x0f\n\x07has_otp\x18\x03 \x01(\x08\x12\x0f\n\x07has_spv\x18\x04 \x01(\x08\x12\x0b\n\x03pin\x18\x05 \x01(\x0c')




_WALLET = descriptor.Descriptor(
  name='Wallet',
  full_name='Wallet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='algo', full_name='Wallet.algo', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='secexp', full_name='Wallet.secexp', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='has_otp', full_name='Wallet.has_otp', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='has_spv', full_name='Wallet.has_spv', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pin', full_name='Wallet.pin', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=30,
  serialized_end=127,
)

_WALLET.fields_by_name['algo'].enum_type = bitkey_pb2._ALGORITHM
DESCRIPTOR.message_types_by_name['Wallet'] = _WALLET

class Wallet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WALLET
  
  # @@protoc_insertion_point(class_scope:Wallet)

# @@protoc_insertion_point(module_scope)
