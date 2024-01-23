# coding: utf-8

"""
    FormKiQ HTTP API

    Formkiq API: Document Management Platform API using OAuth(JWT) Authentication  You can find out more about FormKiQ at [https://formkiq.com](http://formkiq.com).  ## Introduction  FormKiQ is an API-first (head-less), battle-tested document management API. The FormKiQ API provides all the API endpoints to build your Perfect Document Management Platform.  FormKiQ API was built on top of [OpenAPI specification](https://www.openapis.org), so it is easy to use the API spec file with any application that supports the OpenAPI specification.  Open API OAuth Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-jwt.yaml  Open API IAM Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-iam.yaml  ## Authentication FormKiQ offers three forms of authentication:   - OAuth(JWT)   - AWS IAM   - API Key

    The version of the OpenAPI document: 1.13.0
    Contact: support@formkiq.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from formkiq_client.models.only_office_config_document import OnlyOfficeConfigDocument
from formkiq_client.models.only_office_editor_config import OnlyOfficeEditorConfig
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OnlyOfficeConfig(BaseModel):
    """
    OnlyOfficeConfig
    """ # noqa: E501
    only_office_url: Optional[StrictStr] = Field(default=None, description="URL of the ONLYOFFICE application", alias="onlyOfficeUrl")
    token: Optional[StrictStr] = Field(default=None, description="ONLYOFFICE security token")
    document_type: Optional[StrictStr] = Field(default=None, description="Type of document (https://api.onlyoffice.com/editors/config/)", alias="documentType")
    editor_config: Optional[OnlyOfficeEditorConfig] = Field(default=None, alias="editorConfig")
    document: Optional[OnlyOfficeConfigDocument] = None
    __properties: ClassVar[List[str]] = ["onlyOfficeUrl", "token", "documentType", "editorConfig", "document"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OnlyOfficeConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of editor_config
        if self.editor_config:
            _dict['editorConfig'] = self.editor_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document
        if self.document:
            _dict['document'] = self.document.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OnlyOfficeConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "onlyOfficeUrl": obj.get("onlyOfficeUrl"),
            "token": obj.get("token"),
            "documentType": obj.get("documentType"),
            "editorConfig": OnlyOfficeEditorConfig.from_dict(obj.get("editorConfig")) if obj.get("editorConfig") is not None else None,
            "document": OnlyOfficeConfigDocument.from_dict(obj.get("document")) if obj.get("document") is not None else None
        })
        return _obj


