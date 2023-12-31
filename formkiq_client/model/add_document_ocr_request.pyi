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


class AddDocumentOcrRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class parseTypes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'parseTypes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            addPdfDetectedCharactersAsText = schemas.BoolSchema
            __annotations__ = {
                "parseTypes": parseTypes,
                "addPdfDetectedCharactersAsText": addPdfDetectedCharactersAsText,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parseTypes"]) -> MetaOapg.properties.parseTypes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addPdfDetectedCharactersAsText"]) -> MetaOapg.properties.addPdfDetectedCharactersAsText: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["parseTypes", "addPdfDetectedCharactersAsText", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parseTypes"]) -> typing.Union[MetaOapg.properties.parseTypes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addPdfDetectedCharactersAsText"]) -> typing.Union[MetaOapg.properties.addPdfDetectedCharactersAsText, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["parseTypes", "addPdfDetectedCharactersAsText", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        parseTypes: typing.Union[MetaOapg.properties.parseTypes, list, tuple, schemas.Unset] = schemas.unset,
        addPdfDetectedCharactersAsText: typing.Union[MetaOapg.properties.addPdfDetectedCharactersAsText, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AddDocumentOcrRequest':
        return super().__new__(
            cls,
            *_args,
            parseTypes=parseTypes,
            addPdfDetectedCharactersAsText=addPdfDetectedCharactersAsText,
            _configuration=_configuration,
            **kwargs,
        )
