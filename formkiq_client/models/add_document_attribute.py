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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from formkiq_client.models.add_document_attribute_classification import AddDocumentAttributeClassification
from formkiq_client.models.add_document_attribute_standard import AddDocumentAttributeStandard
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

ADDDOCUMENTATTRIBUTE_ONE_OF_SCHEMAS = ["AddDocumentAttributeClassification", "AddDocumentAttributeStandard"]

class AddDocumentAttribute(BaseModel):
    """
    AddDocumentAttribute
    """
    # data type: AddDocumentAttributeStandard
    oneof_schema_1_validator: Optional[AddDocumentAttributeStandard] = None
    # data type: AddDocumentAttributeClassification
    oneof_schema_2_validator: Optional[AddDocumentAttributeClassification] = None
    actual_instance: Optional[Union[AddDocumentAttributeClassification, AddDocumentAttributeStandard]] = None
    one_of_schemas: Set[str] = { "AddDocumentAttributeClassification", "AddDocumentAttributeStandard" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = AddDocumentAttribute.model_construct()
        error_messages = []
        match = 0
        # validate data type: AddDocumentAttributeStandard
        if not isinstance(v, AddDocumentAttributeStandard):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AddDocumentAttributeStandard`")
        else:
            match += 1
        # validate data type: AddDocumentAttributeClassification
        if not isinstance(v, AddDocumentAttributeClassification):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AddDocumentAttributeClassification`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in AddDocumentAttribute with oneOf schemas: AddDocumentAttributeClassification, AddDocumentAttributeStandard. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in AddDocumentAttribute with oneOf schemas: AddDocumentAttributeClassification, AddDocumentAttributeStandard. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into AddDocumentAttributeStandard
        try:
            instance.actual_instance = AddDocumentAttributeStandard.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AddDocumentAttributeClassification
        try:
            instance.actual_instance = AddDocumentAttributeClassification.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into AddDocumentAttribute with oneOf schemas: AddDocumentAttributeClassification, AddDocumentAttributeStandard. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into AddDocumentAttribute with oneOf schemas: AddDocumentAttributeClassification, AddDocumentAttributeStandard. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], AddDocumentAttributeClassification, AddDocumentAttributeStandard]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


