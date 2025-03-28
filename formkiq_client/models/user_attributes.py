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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UserAttributes(BaseModel):
    """
    UserAttributes
    """ # noqa: E501
    address: Optional[StrictStr] = Field(default=None, description="Address of user")
    birthdate: Optional[StrictStr] = Field(default=None, description="Birthdate of user")
    family_name: Optional[StrictStr] = Field(default=None, description="Family name of user", alias="familyName")
    gender: Optional[StrictStr] = Field(default=None, description="Gender of user")
    given_name: Optional[StrictStr] = Field(default=None, description="Given name of user", alias="givenName")
    locale: Optional[StrictStr] = Field(default=None, description="Locale of user")
    middle_name: Optional[StrictStr] = Field(default=None, description="Middle name of user", alias="middleName")
    name: Optional[StrictStr] = Field(default=None, description="Name of user")
    nickname: Optional[StrictStr] = Field(default=None, description="Nickname of user")
    phone_number: Optional[StrictStr] = Field(default=None, description="Phone number of user", alias="phoneNumber")
    picture: Optional[StrictStr] = Field(default=None, description="Picture of user")
    preferred_username: Optional[StrictStr] = Field(default=None, description="Preferred username of user", alias="preferredUsername")
    profile: Optional[StrictStr] = Field(default=None, description="Profile of user")
    zoneinfo: Optional[StrictStr] = Field(default=None, description="Zoneinfo of user")
    updated_at: Optional[StrictStr] = Field(default=None, description="Updated at date of user", alias="updatedAt")
    website: Optional[StrictStr] = Field(default=None, description="Website of user")
    __properties: ClassVar[List[str]] = ["address", "birthdate", "familyName", "gender", "givenName", "locale", "middleName", "name", "nickname", "phoneNumber", "picture", "preferredUsername", "profile", "zoneinfo", "updatedAt", "website"]

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
        """Create an instance of UserAttributes from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "birthdate": obj.get("birthdate"),
            "familyName": obj.get("familyName"),
            "gender": obj.get("gender"),
            "givenName": obj.get("givenName"),
            "locale": obj.get("locale"),
            "middleName": obj.get("middleName"),
            "name": obj.get("name"),
            "nickname": obj.get("nickname"),
            "phoneNumber": obj.get("phoneNumber"),
            "picture": obj.get("picture"),
            "preferredUsername": obj.get("preferredUsername"),
            "profile": obj.get("profile"),
            "zoneinfo": obj.get("zoneinfo"),
            "updatedAt": obj.get("updatedAt"),
            "website": obj.get("website")
        })
        return _obj


