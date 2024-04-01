# coding: utf-8

"""
    FormKiQ API

    Formkiq API: Document Management Platform API using OAuth(JWT) Authentication  You can find out more about FormKiQ at [https://formkiq.com](http://formkiq.com).  ## Introduction  FormKiQ is an API-first (head-less), battle-tested document management API. The FormKiQ API provides all the API endpoints to build your Perfect Document Management Platform.  FormKiQ API was built on top of [OpenAPI specification](https://www.openapis.org), so it is easy to use the API spec file with any application that supports the OpenAPI specification.  Open API OAuth Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-jwt.yaml  Open API IAM Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-iam.yaml  ## Authentication FormKiQ offers three forms of authentication:   - OAuth(JWT)   - AWS IAM   - API Key

    The version of the OpenAPI document: 1.14.0
    Contact: support@formkiq.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from formkiq_client.models.add_document_metadata import AddDocumentMetadata
from formkiq_client.models.add_document_tag import AddDocumentTag
from typing import Optional, Set
from typing_extensions import Self

class AddChildDocument(BaseModel):
    """
    List of related documents
    """ # noqa: E501
    path: Optional[StrictStr] = Field(default=None, description="Path or Name of document")
    deep_link_path: Optional[StrictStr] = Field(default=None, description="Path or Name of deep link", alias="deepLinkPath")
    content_type: Optional[StrictStr] = Field(default=None, description="Document Content-Type", alias="contentType")
    is_base64: Optional[StrictBool] = Field(default=None, description="Is the content Base64-encoded?", alias="isBase64")
    content: StrictStr = Field(description="Document content")
    tags: Optional[List[AddDocumentTag]] = Field(default=None, description="List of document tags")
    metadata: Optional[List[AddDocumentMetadata]] = Field(default=None, description="List of document Metadata")
    __properties: ClassVar[List[str]] = ["path", "deepLinkPath", "contentType", "isBase64", "content", "tags", "metadata"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AddChildDocument from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item in self.metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metadata'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddChildDocument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "path": obj.get("path"),
            "deepLinkPath": obj.get("deepLinkPath"),
            "contentType": obj.get("contentType"),
            "isBase64": obj.get("isBase64"),
            "content": obj.get("content"),
            "tags": [AddDocumentTag.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "metadata": [AddDocumentMetadata.from_dict(_item) for _item in obj["metadata"]] if obj.get("metadata") is not None else None
        })
        return _obj


