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


class TagSchemaOptional(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            key = schemas.StrSchema
            
            
            class defaultValues(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'defaultValues':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class allowedValues(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'allowedValues':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "key": key,
                "defaultValues": defaultValues,
                "allowedValues": allowedValues,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultValues"]) -> MetaOapg.properties.defaultValues: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowedValues"]) -> MetaOapg.properties.allowedValues: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["key", "defaultValues", "allowedValues", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultValues"]) -> typing.Union[MetaOapg.properties.defaultValues, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowedValues"]) -> typing.Union[MetaOapg.properties.allowedValues, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["key", "defaultValues", "allowedValues", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        defaultValues: typing.Union[MetaOapg.properties.defaultValues, list, tuple, schemas.Unset] = schemas.unset,
        allowedValues: typing.Union[MetaOapg.properties.allowedValues, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TagSchemaOptional':
        return super().__new__(
            cls,
            *_args,
            key=key,
            defaultValues=defaultValues,
            allowedValues=allowedValues,
            _configuration=_configuration,
            **kwargs,
        )
