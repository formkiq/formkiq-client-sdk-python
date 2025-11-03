#!/bin/bash

openapi-generator generate \
  -i https://raw.githubusercontent.com/formkiq/formkiq-core/refs/heads/master/docs/openapi/openapi-jwt.yaml \
  -g python \
  -o . \
  --additional-properties=packageName=formkiq_client