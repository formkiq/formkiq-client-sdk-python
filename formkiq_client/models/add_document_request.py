# coding: utf-8

"""
    FormKiQ API JWT

    Formkiq API: Document Management Platform API using OAuth(JWT) Authentication  You can find out more about FormKiQ at [https://formkiq.com](http://formkiq.com).  ## Introduction  FormKiQ is an API-first (head-less), battle-tested document management API. The FormKiQ API provides all the API endpoints to build your Perfect Document Management Platform.  FormKiQ API was built on top of [OpenAPI specification](https://www.openapis.org), so it is easy to use the API spec file with any application that supports the OpenAPI specification.  Open API OAuth Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-jwt.yaml  Open API IAM Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-iam.yaml  ## Authentication FormKiQ offers three forms of authentication:   - OAuth(JWT)   - AWS IAM   - API Key

    The version of the OpenAPI document: 1.16.0
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
from formkiq_client.models.add_action import AddAction
from formkiq_client.models.add_child_document import AddChildDocument
from formkiq_client.models.add_document_attribute import AddDocumentAttribute
from formkiq_client.models.add_document_metadata import AddDocumentMetadata
from formkiq_client.models.add_document_tag import AddDocumentTag
from formkiq_client.models.checksum_type import ChecksumType
from typing import Optional, Set
from typing_extensions import Self

class AddDocumentRequest(BaseModel):
    """
    AddDocumentRequest
    """ # noqa: E501
    document_id: Optional[StrictStr] = Field(default=None, description="optional Document Identifier (Version 4 UUID), if skipped one will be assigned", alias="documentId")
    path: Optional[StrictStr] = Field(default=None, description="Path or Name of document")
    checksum_type: Optional[ChecksumType] = Field(default=None, alias="checksumType")
    checksum: Optional[StrictStr] = Field(default=None, description="The checksum value to validate the file against")
    deep_link_path: Optional[StrictStr] = Field(default=None, description="Path or Name of deep link", alias="deepLinkPath")
    content_type: Optional[StrictStr] = Field(default=None, description="Document media type", alias="contentType")
    is_base64: Optional[StrictBool] = Field(default=None, description="Is the content Base64-encoded?", alias="isBase64")
    content: StrictStr = Field(description="Document content")
    tags: Optional[List[AddDocumentTag]] = Field(default=None, description="List of document tags")
    metadata: Optional[List[AddDocumentMetadata]] = Field(default=None, description="List of document Metadata")
    actions: Optional[List[AddAction]] = Field(default=None, description="List of Actions")
    attributes: Optional[List[AddDocumentAttribute]] = Field(default=None, description="List of Attributes to add to document")
    documents: Optional[List[AddChildDocument]] = Field(default=None, description="List of child documents")
    __properties: ClassVar[List[str]] = ["documentId", "path", "checksumType", "checksum", "deepLinkPath", "contentType", "isBase64", "content", "tags", "metadata", "actions", "attributes", "documents"]

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
        """Create an instance of AddDocumentRequest from a JSON string"""
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
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item_metadata in self.metadata:
                if _item_metadata:
                    _items.append(_item_metadata.to_dict())
            _dict['metadata'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item_actions in self.actions:
                if _item_actions:
                    _items.append(_item_actions.to_dict())
            _dict['actions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item_attributes in self.attributes:
                if _item_attributes:
                    _items.append(_item_attributes.to_dict())
            _dict['attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in documents (list)
        _items = []
        if self.documents:
            for _item_documents in self.documents:
                if _item_documents:
                    _items.append(_item_documents.to_dict())
            _dict['documents'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddDocumentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "documentId": obj.get("documentId"),
            "path": obj.get("path"),
            "checksumType": obj.get("checksumType"),
            "checksum": obj.get("checksum"),
            "deepLinkPath": obj.get("deepLinkPath"),
            "contentType": obj.get("contentType"),
            "isBase64": obj.get("isBase64"),
            "content": obj.get("content"),
            "tags": [AddDocumentTag.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "metadata": [AddDocumentMetadata.from_dict(_item) for _item in obj["metadata"]] if obj.get("metadata") is not None else None,
            "actions": [AddAction.from_dict(_item) for _item in obj["actions"]] if obj.get("actions") is not None else None,
            "attributes": [AddDocumentAttribute.from_dict(_item) for _item in obj["attributes"]] if obj.get("attributes") is not None else None,
            "documents": [AddChildDocument.from_dict(_item) for _item in obj["documents"]] if obj.get("documents") is not None else None
        })
        return _obj


