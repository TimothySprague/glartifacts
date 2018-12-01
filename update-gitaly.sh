#!/bin/sh
git submodule update --remote ext/gitaly-proto

rm -rf glartifacts/gitaly/proto
mkdir -p glartifacts/gitaly/proto
touch glartifacts/gitaly/proto/__init__.py

python3 -m grpc_tools.protoc \
	-Iext/gitaly-proto \
	--python_out=glartifacts/gitaly/proto \
	--grpc_python_out=glartifacts/gitaly/proto \
	ext/gitaly-proto/*.proto

sed -i \
	's/^import \([^ ]*\)_pb2 as \([^ ]*\)$/from . import \1_pb2 as \2/' \
	glartifacts/gitaly/proto/*.py
