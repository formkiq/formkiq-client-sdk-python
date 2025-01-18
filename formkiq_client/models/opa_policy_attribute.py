# coding: utf-8

"""
    FormKiQ API JWT

    Formkiq API: Document Management Platform API using OAuth(JWT) Authentication  You can find out more about FormKiQ at [https://formkiq.com](http://formkiq.com).  ## Introduction  FormKiQ is an API-first (head-less), battle-tested document management API. The FormKiQ API provides all the API endpoints to build your Perfect Document Management Platform.  FormKiQ API was built on top of [OpenAPI specification](https://www.openapis.org), so it is easy to use the API spec file with any application that supports the OpenAPI specification.  Open API OAuth Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-jwt.yaml  Open API IAM Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-iam.yaml  ## Authentication FormKiQ offers three forms of authentication:   - OAuth(JWT)   - AWS IAM   - API Key

    The version of the OpenAPI document: 1.16.1
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
from formkiq_client.models.opa_policy_attribute_eq import OpaPolicyAttributeEq
from formkiq_client.models.opa_policy_attribute_gt import OpaPolicyAttributeGt
from formkiq_client.models.opa_policy_attribute_gte import OpaPolicyAttributeGte
from formkiq_client.models.opa_policy_attribute_lt import OpaPolicyAttributeLt
from formkiq_client.models.opa_policy_attribute_lte import OpaPolicyAttributeLte
from formkiq_client.models.opa_policy_attribute_neq import OpaPolicyAttributeNeq
from typing import Optional, Set
from typing_extensions import Self

class OpaPolicyAttribute(BaseModel):
    """
    OpaPolicyAttribute
    """ # noqa: E501
    key: Optional[StrictStr] = Field(default=None, description="Attribute Key")
    eq: Optional[OpaPolicyAttributeEq] = None
    gt: Optional[OpaPolicyAttributeGt] = None
    gte: Optional[OpaPolicyAttributeGte] = None
    lt: Optional[OpaPolicyAttributeLt] = None
    lte: Optional[OpaPolicyAttributeLte] = None
    neq: Optional[OpaPolicyAttributeNeq] = None
    __properties: ClassVar[List[str]] = ["key", "eq", "gt", "gte", "lt", "lte", "neq"]

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
        """Create an instance of OpaPolicyAttribute from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of gt
        if self.gt:
            _dict['gt'] = self.gt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gte
        if self.gte:
            _dict['gte'] = self.gte.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lt
        if self.lt:
            _dict['lt'] = self.lt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lte
        if self.lte:
            _dict['lte'] = self.lte.to_dict()
        # override the default output from pydantic by calling `to_dict()` of neq
        if self.neq:
            _dict['neq'] = self.neq.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OpaPolicyAttribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "key": obj.get("key"),
            "eq": OpaPolicyAttributeEq.from_dict(obj["eq"]) if obj.get("eq") is not None else None,
            "gt": OpaPolicyAttributeGt.from_dict(obj["gt"]) if obj.get("gt") is not None else None,
            "gte": OpaPolicyAttributeGte.from_dict(obj["gte"]) if obj.get("gte") is not None else None,
            "lt": OpaPolicyAttributeLt.from_dict(obj["lt"]) if obj.get("lt") is not None else None,
            "lte": OpaPolicyAttributeLte.from_dict(obj["lte"]) if obj.get("lte") is not None else None,
            "neq": OpaPolicyAttributeNeq.from_dict(obj["neq"]) if obj.get("neq") is not None else None
        })
        return _obj


