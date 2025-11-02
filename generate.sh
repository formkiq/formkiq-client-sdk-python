#!/bin/bash

openapi-generator generate -g python -i https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-jwt.yaml -o . --additional-properties packageUrl=https://github.com/formkiq/formkiq-client-sdk-python --additional-properties projectName=formkiq-client
