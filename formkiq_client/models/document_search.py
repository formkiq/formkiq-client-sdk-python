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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from formkiq_client.models.document_search_attribute import DocumentSearchAttribute
from formkiq_client.models.document_search_meta import DocumentSearchMeta
from formkiq_client.models.document_search_tag import DocumentSearchTag
from formkiq_client.models.document_search_tags import DocumentSearchTags
from typing import Optional, Set
from typing_extensions import Self

class DocumentSearch(BaseModel):
    """
    Document tag search criteria
    """ # noqa: E501
    text: Optional[StrictStr] = Field(default=None, description="Full text search")
    meta: Optional[DocumentSearchMeta] = None
    attribute: Optional[DocumentSearchAttribute] = None
    attributes: Optional[List[DocumentSearchAttribute]] = Field(default=None, description="List of Composite Key attributes to filter search results on")
    tag: Optional[DocumentSearchTag] = None
    tags: Optional[List[DocumentSearchTags]] = Field(default=None, description="List of Composite Key tags to filter search results on")
    document_ids: Optional[List[StrictStr]] = Field(default=None, description="List of DocumentIds to filter search results on", alias="documentIds")
    __properties: ClassVar[List[str]] = ["text", "meta", "attribute", "attributes", "tag", "tags", "documentIds"]

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
        """Create an instance of DocumentSearch from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attribute
        if self.attribute:
            _dict['attribute'] = self.attribute.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item in self.attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of tag
        if self.tag:
            _dict['tag'] = self.tag.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocumentSearch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "text": obj.get("text"),
            "meta": DocumentSearchMeta.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
            "attribute": DocumentSearchAttribute.from_dict(obj["attribute"]) if obj.get("attribute") is not None else None,
            "attributes": [DocumentSearchAttribute.from_dict(_item) for _item in obj["attributes"]] if obj.get("attributes") is not None else None,
            "tag": DocumentSearchTag.from_dict(obj["tag"]) if obj.get("tag") is not None else None,
            "tags": [DocumentSearchTags.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "documentIds": obj.get("documentIds")
        })
        return _obj


