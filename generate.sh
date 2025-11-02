#!/bin/bash

openapi-generator generate \
  -g python \
  -i https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-jwt.yaml \
  -o . \
  --additional-properties packageName=openapi_client,packageUrl=https://github.com/formkiq/formkiq-client-sdk-python,projectName=formkiq-client \
  --model-package model