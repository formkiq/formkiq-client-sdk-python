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


class GetTagSchemasRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class schemas(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TagSchemaSummary']:
                        return TagSchemaSummary
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TagSchemaSummary'], typing.List['TagSchemaSummary']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'schemas':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TagSchemaSummary':
                    return super().__getitem__(i)
            next = schemas.StrSchema
            previous = schemas.StrSchema
            __annotations__ = {
                "schemas": schemas,
                "next": next,
                "previous": previous,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schemas"]) -> MetaOapg.properties.schemas: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next"]) -> MetaOapg.properties.next: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["previous"]) -> MetaOapg.properties.previous: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["schemas", "next", "previous", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schemas"]) -> typing.Union[MetaOapg.properties.schemas, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next"]) -> typing.Union[MetaOapg.properties.next, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["previous"]) -> typing.Union[MetaOapg.properties.previous, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["schemas", "next", "previous", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        schemas: typing.Union[MetaOapg.properties.schemas, list, tuple, schemas.Unset] = schemas.unset,
        next: typing.Union[MetaOapg.properties.next, str, schemas.Unset] = schemas.unset,
        previous: typing.Union[MetaOapg.properties.previous, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetTagSchemasRequest':
        return super().__new__(
            cls,
            *_args,
            schemas=schemas,
            next=next,
            previous=previous,
            _configuration=_configuration,
            **kwargs,
        )

from formkiq_client.model.tag_schema_summary import TagSchemaSummary
