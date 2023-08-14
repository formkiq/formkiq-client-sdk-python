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


class GetDocumentSync(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class service(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "TYPESENSE": "TYPESENSE",
                        "OPENSEARCH": "OPENSEARCH",
                    }
                
                @schemas.classproperty
                def TYPESENSE(cls):
                    return cls("TYPESENSE")
                
                @schemas.classproperty
                def OPENSEARCH(cls):
                    return cls("OPENSEARCH")
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "COMPLETE": "COMPLETE",
                        "FAILED": "FAILED",
                    }
                
                @schemas.classproperty
                def COMPLETE(cls):
                    return cls("COMPLETE")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("FAILED")
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "METADATA": "METADATA",
                        "TAG": "TAG",
                    }
                
                @schemas.classproperty
                def METADATA(cls):
                    return cls("METADATA")
                
                @schemas.classproperty
                def TAG(cls):
                    return cls("TAG")
            syncDate = schemas.StrSchema
            userId = schemas.StrSchema
            message = schemas.StrSchema
            __annotations__ = {
                "service": service,
                "status": status,
                "type": type,
                "syncDate": syncDate,
                "userId": userId,
                "message": message,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["service"]) -> MetaOapg.properties.service: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["syncDate"]) -> MetaOapg.properties.syncDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["service", "status", "type", "syncDate", "userId", "message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["service"]) -> typing.Union[MetaOapg.properties.service, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["syncDate"]) -> typing.Union[MetaOapg.properties.syncDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["service", "status", "type", "syncDate", "userId", "message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        service: typing.Union[MetaOapg.properties.service, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        syncDate: typing.Union[MetaOapg.properties.syncDate, str, schemas.Unset] = schemas.unset,
        userId: typing.Union[MetaOapg.properties.userId, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetDocumentSync':
        return super().__new__(
            cls,
            *_args,
            service=service,
            status=status,
            type=type,
            syncDate=syncDate,
            userId=userId,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )