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


class DocumentSearchItemMeta(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            folder = schemas.StrSchema
            path = schemas.StrSchema
            
            
            class indexType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "folder": "FOLDER",
                    }
                
                @schemas.classproperty
                def FOLDER(cls):
                    return cls("folder")
            indexFilterBeginsWith = schemas.StrSchema
            __annotations__ = {
                "folder": folder,
                "path": path,
                "indexType": indexType,
                "indexFilterBeginsWith": indexFilterBeginsWith,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder"]) -> MetaOapg.properties.folder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["indexType"]) -> MetaOapg.properties.indexType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["indexFilterBeginsWith"]) -> MetaOapg.properties.indexFilterBeginsWith: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["folder", "path", "indexType", "indexFilterBeginsWith", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder"]) -> typing.Union[MetaOapg.properties.folder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["indexType"]) -> typing.Union[MetaOapg.properties.indexType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["indexFilterBeginsWith"]) -> typing.Union[MetaOapg.properties.indexFilterBeginsWith, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["folder", "path", "indexType", "indexFilterBeginsWith", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        folder: typing.Union[MetaOapg.properties.folder, str, schemas.Unset] = schemas.unset,
        path: typing.Union[MetaOapg.properties.path, str, schemas.Unset] = schemas.unset,
        indexType: typing.Union[MetaOapg.properties.indexType, str, schemas.Unset] = schemas.unset,
        indexFilterBeginsWith: typing.Union[MetaOapg.properties.indexFilterBeginsWith, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentSearchItemMeta':
        return super().__new__(
            cls,
            *_args,
            folder=folder,
            path=path,
            indexType=indexType,
            indexFilterBeginsWith=indexFilterBeginsWith,
            _configuration=_configuration,
            **kwargs,
        )
