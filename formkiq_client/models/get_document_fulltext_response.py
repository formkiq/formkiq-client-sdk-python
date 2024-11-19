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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from formkiq_client.models.fulltext_attribute import FulltextAttribute
from typing import Optional, Set
from typing_extensions import Self

class GetDocumentFulltextResponse(BaseModel):
    """
    GetDocumentFulltextResponse
    """ # noqa: E501
    site_id: Optional[StrictStr] = Field(default=None, description="Site Identifier", alias="siteId")
    content: Optional[StrictStr] = Field(default=None, description="Content of document")
    content_type: Optional[StrictStr] = Field(default=None, description="Document Content-Type", alias="contentType")
    path: Optional[StrictStr] = Field(default=None, description="Path or Name of document")
    deep_link_path: Optional[StrictStr] = Field(default=None, description="Path or Name of deep link", alias="deepLinkPath")
    inserted_date: Optional[StrictStr] = Field(default=None, description="Inserted Timestamp", alias="insertedDate")
    last_modified_date: Optional[StrictStr] = Field(default=None, description="Last Modified Timestamp", alias="lastModifiedDate")
    document_id: Optional[StrictStr] = Field(default=None, description="Document Identifier", alias="documentId")
    created_by: Optional[StrictStr] = Field(default=None, description="User who added document", alias="createdBy")
    content_length: Optional[StrictInt] = Field(default=None, description="Document size", alias="contentLength")
    tags: Optional[Dict[str, Dict[str, Any]]] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = None
    attributes: Optional[Dict[str, FulltextAttribute]] = None
    __properties: ClassVar[List[str]] = ["siteId", "content", "contentType", "path", "deepLinkPath", "insertedDate", "lastModifiedDate", "documentId", "createdBy", "contentLength", "tags", "metadata", "attributes"]

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
        """Create an instance of GetDocumentFulltextResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in attributes (dict)
        _field_dict = {}
        if self.attributes:
            for _key_attributes in self.attributes:
                if self.attributes[_key_attributes]:
                    _field_dict[_key_attributes] = self.attributes[_key_attributes].to_dict()
            _dict['attributes'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetDocumentFulltextResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "siteId": obj.get("siteId"),
            "content": obj.get("content"),
            "contentType": obj.get("contentType"),
            "path": obj.get("path"),
            "deepLinkPath": obj.get("deepLinkPath"),
            "insertedDate": obj.get("insertedDate"),
            "lastModifiedDate": obj.get("lastModifiedDate"),
            "documentId": obj.get("documentId"),
            "createdBy": obj.get("createdBy"),
            "contentLength": obj.get("contentLength"),
            "tags": obj.get("tags"),
            "metadata": obj.get("metadata"),
            "attributes": dict(
                (_k, FulltextAttribute.from_dict(_v))
                for _k, _v in obj["attributes"].items()
            )
            if obj.get("attributes") is not None
            else None
        })
        return _obj


