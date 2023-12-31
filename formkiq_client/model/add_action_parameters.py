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


class AddActionParameters(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            ocrParseTypes = schemas.StrSchema
            addPdfDetectedCharactersAsText = schemas.BoolSchema
            url = schemas.StrSchema
            characterMax = schemas.StrSchema
            
            
            class engine(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "chatgpt": "CHATGPT",
                    }
                
                @schemas.classproperty
                def CHATGPT(cls):
                    return cls("chatgpt")
            tags = schemas.StrSchema
            __annotations__ = {
                "ocrParseTypes": ocrParseTypes,
                "addPdfDetectedCharactersAsText": addPdfDetectedCharactersAsText,
                "url": url,
                "characterMax": characterMax,
                "engine": engine,
                "tags": tags,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ocrParseTypes"]) -> MetaOapg.properties.ocrParseTypes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addPdfDetectedCharactersAsText"]) -> MetaOapg.properties.addPdfDetectedCharactersAsText: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["characterMax"]) -> MetaOapg.properties.characterMax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["engine"]) -> MetaOapg.properties.engine: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ocrParseTypes", "addPdfDetectedCharactersAsText", "url", "characterMax", "engine", "tags", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ocrParseTypes"]) -> typing.Union[MetaOapg.properties.ocrParseTypes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addPdfDetectedCharactersAsText"]) -> typing.Union[MetaOapg.properties.addPdfDetectedCharactersAsText, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["characterMax"]) -> typing.Union[MetaOapg.properties.characterMax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["engine"]) -> typing.Union[MetaOapg.properties.engine, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ocrParseTypes", "addPdfDetectedCharactersAsText", "url", "characterMax", "engine", "tags", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        ocrParseTypes: typing.Union[MetaOapg.properties.ocrParseTypes, str, schemas.Unset] = schemas.unset,
        addPdfDetectedCharactersAsText: typing.Union[MetaOapg.properties.addPdfDetectedCharactersAsText, bool, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        characterMax: typing.Union[MetaOapg.properties.characterMax, str, schemas.Unset] = schemas.unset,
        engine: typing.Union[MetaOapg.properties.engine, str, schemas.Unset] = schemas.unset,
        tags: typing.Union[MetaOapg.properties.tags, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AddActionParameters':
        return super().__new__(
            cls,
            *_args,
            ocrParseTypes=ocrParseTypes,
            addPdfDetectedCharactersAsText=addPdfDetectedCharactersAsText,
            url=url,
            characterMax=characterMax,
            engine=engine,
            tags=tags,
            _configuration=_configuration,
            **kwargs,
        )
