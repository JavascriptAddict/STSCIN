# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: estate.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'estate.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x65state.proto\x12\x06\x45state\"\xa0\x01\n\x0c\x45stateFilter\x12\r\n\x05state\x18\x01 \x01(\t\x12\x15\n\rresidenceName\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x1c\n\x14startTransactionDate\x18\x04 \x01(\t\x12\x1a\n\x12\x65ndTransactionDate\x18\x05 \x01(\t\x12\x10\n\x08minPrice\x18\x06 \x01(\x02\x12\x10\n\x08maxPrice\x18\x07 \x01(\x02\"\x88\x01\n\nEstateData\x12\r\n\x05state\x18\x01 \x01(\t\x12\x0c\n\x04\x61rea\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x17\n\x0ftransactionDate\x18\x04 \x01(\t\x12\r\n\x05price\x18\x05 \x01(\x02\x12\x10\n\x08\x65stateId\x18\x06 \x01(\t\x12\x15\n\rresidenceName\x18\x07 \x01(\t\"1\n\nEstateList\x12#\n\x07\x65states\x18\x01 \x03(\x0b\x32\x12.Estate.EstateData2\xf7\x01\n\x06\x45state\x12\x38\n\x0cGetAllEstate\x12\x12.Estate.EstateData\x1a\x12.Estate.EstateList\"\x00\x12?\n\x11GetFilteredEstate\x12\x14.Estate.EstateFilter\x1a\x12.Estate.EstateList\"\x00\x12\x38\n\x0c\x43reateEstate\x12\x12.Estate.EstateData\x1a\x12.Estate.EstateData\"\x00\x12\x38\n\x0cUpdateEstate\x12\x12.Estate.EstateData\x1a\x12.Estate.EstateData\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'estate_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ESTATEFILTER']._serialized_start=25
  _globals['_ESTATEFILTER']._serialized_end=185
  _globals['_ESTATEDATA']._serialized_start=188
  _globals['_ESTATEDATA']._serialized_end=324
  _globals['_ESTATELIST']._serialized_start=326
  _globals['_ESTATELIST']._serialized_end=375
  _globals['_ESTATE']._serialized_start=378
  _globals['_ESTATE']._serialized_end=625
# @@protoc_insertion_point(module_scope)