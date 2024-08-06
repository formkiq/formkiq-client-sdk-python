# coding: utf-8

"""
    FormKiQ API

    Formkiq API: Document Management Platform API using OAuth(JWT) Authentication  You can find out more about FormKiQ at [https://formkiq.com](http://formkiq.com).  ## Introduction  FormKiQ is an API-first (head-less), battle-tested document management API. The FormKiQ API provides all the API endpoints to build your Perfect Document Management Platform.  FormKiQ API was built on top of [OpenAPI specification](https://www.openapis.org), so it is easy to use the API spec file with any application that supports the OpenAPI specification.  Open API OAuth Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-jwt.yaml  Open API IAM Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-iam.yaml  ## Authentication FormKiQ offers three forms of authentication:   - OAuth(JWT)   - AWS IAM   - API Key

    The version of the OpenAPI document: 1.15.1
    Contact: support@formkiq.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from formkiq_client.models.tag_schema_composite_key import TagSchemaCompositeKey
from formkiq_client.models.tag_schema_optional import TagSchemaOptional
from formkiq_client.models.tag_schema_required import TagSchemaRequired
from typing import Optional, Set
from typing_extensions import Self

class TagSchemaTags(BaseModel):
    """
    TagSchemaTags
    """ # noqa: E501
    composite_keys: Optional[List[TagSchemaCompositeKey]] = Field(default=None, description="List of Composite Keys", alias="compositeKeys")
    required: Optional[List[TagSchemaRequired]] = Field(default=None, description="List of Required Tags")
    optional: Optional[List[TagSchemaOptional]] = Field(default=None, description="List of Optional Tags")
    allow_additional_tags: Optional[StrictBool] = Field(default=True, alias="allowAdditionalTags")
    __properties: ClassVar[List[str]] = ["compositeKeys", "required", "optional", "allowAdditionalTags"]

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
        """Create an instance of TagSchemaTags from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in composite_keys (list)
        _items = []
        if self.composite_keys:
            for _item in self.composite_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['compositeKeys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in required (list)
        _items = []
        if self.required:
            for _item in self.required:
                if _item:
                    _items.append(_item.to_dict())
            _dict['required'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in optional (list)
        _items = []
        if self.optional:
            for _item in self.optional:
                if _item:
                    _items.append(_item.to_dict())
            _dict['optional'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TagSchemaTags from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "compositeKeys": [TagSchemaCompositeKey.from_dict(_item) for _item in obj["compositeKeys"]] if obj.get("compositeKeys") is not None else None,
            "required": [TagSchemaRequired.from_dict(_item) for _item in obj["required"]] if obj.get("required") is not None else None,
            "optional": [TagSchemaOptional.from_dict(_item) for _item in obj["optional"]] if obj.get("optional") is not None else None,
            "allowAdditionalTags": obj.get("allowAdditionalTags") if obj.get("allowAdditionalTags") is not None else True
        })
        return _obj


