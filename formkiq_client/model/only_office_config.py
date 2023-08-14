# coding: utf-8

"""
    FormKiQ HTTP API

    Formkiq API: Document Management Platform API using JWT Authentication  # noqa: E501

    The version of the OpenAPI document: 1.12.0
    Contact: support@formkiq.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from formkiq_client import schemas  # noqa: F401


class OnlyOfficeConfig(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            onlyOfficeUrl = schemas.StrSchema
            token = schemas.StrSchema
            documentType = schemas.StrSchema
        
            @staticmethod
            def editorConfig() -> typing.Type['OnlyOfficeEditorConfig']:
                return OnlyOfficeEditorConfig
        
            @staticmethod
            def document() -> typing.Type['OnlyOfficeConfigDocument']:
                return OnlyOfficeConfigDocument
            __annotations__ = {
                "onlyOfficeUrl": onlyOfficeUrl,
                "token": token,
                "documentType": documentType,
                "editorConfig": editorConfig,
                "document": document,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onlyOfficeUrl"]) -> MetaOapg.properties.onlyOfficeUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentType"]) -> MetaOapg.properties.documentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["editorConfig"]) -> 'OnlyOfficeEditorConfig': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["document"]) -> 'OnlyOfficeConfigDocument': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["onlyOfficeUrl", "token", "documentType", "editorConfig", "document", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onlyOfficeUrl"]) -> typing.Union[MetaOapg.properties.onlyOfficeUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> typing.Union[MetaOapg.properties.token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentType"]) -> typing.Union[MetaOapg.properties.documentType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["editorConfig"]) -> typing.Union['OnlyOfficeEditorConfig', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["document"]) -> typing.Union['OnlyOfficeConfigDocument', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["onlyOfficeUrl", "token", "documentType", "editorConfig", "document", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        onlyOfficeUrl: typing.Union[MetaOapg.properties.onlyOfficeUrl, str, schemas.Unset] = schemas.unset,
        token: typing.Union[MetaOapg.properties.token, str, schemas.Unset] = schemas.unset,
        documentType: typing.Union[MetaOapg.properties.documentType, str, schemas.Unset] = schemas.unset,
        editorConfig: typing.Union['OnlyOfficeEditorConfig', schemas.Unset] = schemas.unset,
        document: typing.Union['OnlyOfficeConfigDocument', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OnlyOfficeConfig':
        return super().__new__(
            cls,
            *_args,
            onlyOfficeUrl=onlyOfficeUrl,
            token=token,
            documentType=documentType,
            editorConfig=editorConfig,
            document=document,
            _configuration=_configuration,
            **kwargs,
        )

from formkiq_client.model.only_office_config_document import OnlyOfficeConfigDocument
from formkiq_client.model.only_office_editor_config import OnlyOfficeEditorConfig