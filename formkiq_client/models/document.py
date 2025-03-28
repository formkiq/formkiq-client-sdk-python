# coding: utf-8

"""
    FormKiQ API JWT

    Formkiq API: Document Management Platform API using OAuth(JWT) Authentication  You can find out more about FormKiQ at [https://formkiq.com](http://formkiq.com).  ## Introduction  FormKiQ is an API-first (head-less), battle-tested document management API. The FormKiQ API provides all the API endpoints to build your Perfect Document Management Platform.  FormKiQ API was built on top of [OpenAPI specification](https://www.openapis.org), so it is easy to use the API spec file with any application that supports the OpenAPI specification.  Open API OAuth Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-jwt.yaml  Open API IAM Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-iam.yaml  ## Authentication FormKiQ offers three forms of authentication:   - OAuth(JWT)   - AWS IAM   - API Key

    The version of the OpenAPI document: 1.17.0
    Contact: support@formkiq.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from formkiq_client.models.checksum_type import ChecksumType
from formkiq_client.models.document_metadata import DocumentMetadata
from typing import Optional, Set
from typing_extensions import Self

class Document(BaseModel):
    """
    Document
    """ # noqa: E501
    site_id: Optional[StrictStr] = Field(default=None, description="Site Identifier", alias="siteId")
    path: Optional[StrictStr] = Field(default=None, description="Path or Name of document")
    width: Optional[StrictStr] = Field(default=None, description="Document Content Width property")
    height: Optional[StrictStr] = Field(default=None, description="Document Content Height property")
    deep_link_path: Optional[StrictStr] = Field(default=None, description="Path or Name of deep link", alias="deepLinkPath")
    inserted_date: Optional[StrictStr] = Field(default=None, description="Inserted Timestamp", alias="insertedDate")
    last_modified_date: Optional[StrictStr] = Field(default=None, description="Last Modified Timestamp", alias="lastModifiedDate")
    checksum: Optional[StrictStr] = Field(default=None, description="Document checksum, changes when document file changes")
    checksum_type: Optional[ChecksumType] = Field(default=None, alias="checksumType")
    document_id: Optional[StrictStr] = Field(default=None, description="Document Identifier", alias="documentId")
    content_type: Optional[StrictStr] = Field(default=None, description="Document Content-Type", alias="contentType")
    user_id: Optional[StrictStr] = Field(default=None, description="User who added document", alias="userId")
    content_length: Optional[StrictInt] = Field(default=None, description="Document size", alias="contentLength")
    version: Optional[StrictStr] = Field(default=None, description="Document version")
    version_key: Optional[StrictStr] = Field(default=None, description="Document Version Identifier", alias="versionKey")
    s3version: Optional[StrictStr] = Field(default=None, description="Document storage version")
    belongs_to_document_id: Optional[StrictStr] = Field(default=None, description="Parent Document Identifier", alias="belongsToDocumentId")
    metadata: Optional[List[DocumentMetadata]] = Field(default=None, description="List of document Metadata")
    __properties: ClassVar[List[str]] = ["siteId", "path", "width", "height", "deepLinkPath", "insertedDate", "lastModifiedDate", "checksum", "checksumType", "documentId", "contentType", "userId", "contentLength", "version", "versionKey", "s3version", "belongsToDocumentId", "metadata"]

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
        """Create an instance of Document from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item_metadata in self.metadata:
                if _item_metadata:
                    _items.append(_item_metadata.to_dict())
            _dict['metadata'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Document from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "siteId": obj.get("siteId"),
            "path": obj.get("path"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "deepLinkPath": obj.get("deepLinkPath"),
            "insertedDate": obj.get("insertedDate"),
            "lastModifiedDate": obj.get("lastModifiedDate"),
            "checksum": obj.get("checksum"),
            "checksumType": obj.get("checksumType"),
            "documentId": obj.get("documentId"),
            "contentType": obj.get("contentType"),
            "userId": obj.get("userId"),
            "contentLength": obj.get("contentLength"),
            "version": obj.get("version"),
            "versionKey": obj.get("versionKey"),
            "s3version": obj.get("s3version"),
            "belongsToDocumentId": obj.get("belongsToDocumentId"),
            "metadata": [DocumentMetadata.from_dict(_item) for _item in obj["metadata"]] if obj.get("metadata") is not None else None
        })
        return _obj


