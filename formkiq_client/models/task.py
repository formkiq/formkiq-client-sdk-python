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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from formkiq_client.models.task_status import TaskStatus
from typing import Optional, Set
from typing_extensions import Self

class Task(BaseModel):
    """
    Task
    """ # noqa: E501
    task_id: Optional[StrictStr] = Field(default=None, description="Task Identifier", alias="taskId")
    inserted_date: Optional[StrictStr] = Field(default=None, description="Inserted Timestamp", alias="insertedDate")
    name: Optional[StrictStr] = Field(default=None, description="Name of Task")
    description: Optional[StrictStr] = Field(default=None, description="Description of Task")
    start_date: Optional[StrictStr] = Field(default=None, description="Start Date of Task", alias="startDate")
    end_date: Optional[StrictStr] = Field(default=None, description="End Date of Task", alias="endDate")
    user_id: Optional[StrictStr] = Field(default=None, description="User who added Task", alias="userId")
    status: Optional[TaskStatus] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = None
    __properties: ClassVar[List[str]] = ["taskId", "insertedDate", "name", "description", "startDate", "endDate", "userId", "status", "metadata"]

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
        """Create an instance of Task from a JSON string"""
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
        """Create an instance of Task from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "taskId": obj.get("taskId"),
            "insertedDate": obj.get("insertedDate"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "userId": obj.get("userId"),
            "status": obj.get("status"),
            "metadata": obj.get("metadata")
        })
        return _obj


