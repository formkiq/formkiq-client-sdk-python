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
from formkiq_client.models.document_fulltext_attribute_eq import DocumentFulltextAttributeEq
from typing import Optional, Set
from typing_extensions import Self

class DocumentFulltextAttribute(BaseModel):
    """
    DocumentFulltextAttribute
    """ # noqa: E501
    eq: Optional[DocumentFulltextAttributeEq] = None
    eq_or: Optional[List[DocumentFulltextAttributeEq]] = Field(default=None, description="Searches for ANY strings that eq", alias="eqOr")
    key: StrictStr = Field(description="Tag key to search")
    __properties: ClassVar[List[str]] = ["eq", "eqOr", "key"]

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
        """Create an instance of DocumentFulltextAttribute from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of eq
        if self.eq:
            _dict['eq'] = self.eq.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in eq_or (list)
        _items = []
        if self.eq_or:
            for _item in self.eq_or:
                if _item:
                    _items.append(_item.to_dict())
            _dict['eqOr'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocumentFulltextAttribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eq": DocumentFulltextAttributeEq.from_dict(obj["eq"]) if obj.get("eq") is not None else None,
            "eqOr": [DocumentFulltextAttributeEq.from_dict(_item) for _item in obj["eqOr"]] if obj.get("eqOr") is not None else None,
            "key": obj.get("key")
        })
        return _obj


