# coding: utf-8

"""
    FormKiQ API

    Formkiq API: Document Management Platform API using OAuth(JWT) Authentication  You can find out more about FormKiQ at [https://formkiq.com](http://formkiq.com).  ## Introduction  FormKiQ is an API-first (head-less), battle-tested document management API. The FormKiQ API provides all the API endpoints to build your Perfect Document Management Platform.  FormKiQ API was built on top of [OpenAPI specification](https://www.openapis.org), so it is easy to use the API spec file with any application that supports the OpenAPI specification.  Open API OAuth Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-jwt.yaml  Open API IAM Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-iam.yaml  ## Authentication FormKiQ offers three forms of authentication:   - OAuth(JWT)   - AWS IAM   - API Key

    The version of the OpenAPI document: 1.15.0
    Contact: support@formkiq.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DocumentActionType(str, Enum):
    """
    Type of the Document Action
    """

    """
    allowed enum values
    """
    ANTIVIRUS = 'ANTIVIRUS'
    DOCUMENTTAGGING = 'DOCUMENTTAGGING'
    FULLTEXT = 'FULLTEXT'
    NOTIFICATION = 'NOTIFICATION'
    OCR = 'OCR'
    QUEUE = 'QUEUE'
    WEBHOOK = 'WEBHOOK'
    IDP = 'IDP'
    PUBLISH = 'PUBLISH'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DocumentActionType from a JSON string"""
        return cls(json.loads(json_str))


