#!/bin/bash

openapi-generator generate \
  -i https://raw.githubusercontent.com/formkiq/formkiq-core/refs/heads/master/docs/openapi/openapi-jwt.yaml \
  -g python \
  --git-user-id formkiq --git-repo-id formkiq-client-sdk-python \
  -o . \
  --additional-properties=packageName=formkiq_client