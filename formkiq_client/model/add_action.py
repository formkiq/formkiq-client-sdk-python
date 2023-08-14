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


class AddAction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "OCR": "OCR",
                        "FULLTEXT": "FULLTEXT",
                        "ANTIVIRUS": "ANTIVIRUS",
                        "WEBHOOK": "WEBHOOK",
                        "DOCUMENTTAGGING": "DOCUMENTTAGGING",
                    }
                
                @schemas.classproperty
                def OCR(cls):
                    return cls("OCR")
                
                @schemas.classproperty
                def FULLTEXT(cls):
                    return cls("FULLTEXT")
                
                @schemas.classproperty
                def ANTIVIRUS(cls):
                    return cls("ANTIVIRUS")
                
                @schemas.classproperty
                def WEBHOOK(cls):
                    return cls("WEBHOOK")
                
                @schemas.classproperty
                def DOCUMENTTAGGING(cls):
                    return cls("DOCUMENTTAGGING")
        
            @staticmethod
            def parameters() -> typing.Type['AddActionParameters']:
                return AddActionParameters
            __annotations__ = {
                "type": type,
                "parameters": parameters,
            }
    
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parameters"]) -> 'AddActionParameters': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "parameters", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parameters"]) -> typing.Union['AddActionParameters', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "parameters", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        parameters: typing.Union['AddActionParameters', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AddAction':
        return super().__new__(
            cls,
            *_args,
            type=type,
            parameters=parameters,
            _configuration=_configuration,
            **kwargs,
        )

from formkiq_client.model.add_action_parameters import AddActionParameters
