# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yolox.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0byolox.proto\x12\x05yolox\";\n\x08\x42\x36\x34Image\x12\x10\n\x08\x62\x36\x34image\x18\x01 \x01(\t\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\"\x1e\n\nPrediction\x12\x10\n\x08\x62\x62ox_arr\x18\x02 \x01(\t2:\n\x05Yolox\x12\x31\n\tInference\x12\x0f.yolox.B64Image\x1a\x11.yolox.Prediction\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yolox_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _B64IMAGE._serialized_start=22
  _B64IMAGE._serialized_end=81
  _PREDICTION._serialized_start=83
  _PREDICTION._serialized_end=113
  _YOLOX._serialized_start=115
  _YOLOX._serialized_end=173
# @@protoc_insertion_point(module_scope)
