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


class SetConfigRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            chatGptApiKey = schemas.StrSchema
            maxContentLengthBytes = schemas.StrSchema
            maxDocuments = schemas.StrSchema
            maxWebhooks = schemas.StrSchema
            __annotations__ = {
                "chatGptApiKey": chatGptApiKey,
                "maxContentLengthBytes": maxContentLengthBytes,
                "maxDocuments": maxDocuments,
                "maxWebhooks": maxWebhooks,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chatGptApiKey"]) -> MetaOapg.properties.chatGptApiKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxContentLengthBytes"]) -> MetaOapg.properties.maxContentLengthBytes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxDocuments"]) -> MetaOapg.properties.maxDocuments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxWebhooks"]) -> MetaOapg.properties.maxWebhooks: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["chatGptApiKey", "maxContentLengthBytes", "maxDocuments", "maxWebhooks", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chatGptApiKey"]) -> typing.Union[MetaOapg.properties.chatGptApiKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxContentLengthBytes"]) -> typing.Union[MetaOapg.properties.maxContentLengthBytes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxDocuments"]) -> typing.Union[MetaOapg.properties.maxDocuments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxWebhooks"]) -> typing.Union[MetaOapg.properties.maxWebhooks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["chatGptApiKey", "maxContentLengthBytes", "maxDocuments", "maxWebhooks", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        chatGptApiKey: typing.Union[MetaOapg.properties.chatGptApiKey, str, schemas.Unset] = schemas.unset,
        maxContentLengthBytes: typing.Union[MetaOapg.properties.maxContentLengthBytes, str, schemas.Unset] = schemas.unset,
        maxDocuments: typing.Union[MetaOapg.properties.maxDocuments, str, schemas.Unset] = schemas.unset,
        maxWebhooks: typing.Union[MetaOapg.properties.maxWebhooks, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SetConfigRequest':
        return super().__new__(
            cls,
            *_args,
            chatGptApiKey=chatGptApiKey,
            maxContentLengthBytes=maxContentLengthBytes,
            maxDocuments=maxDocuments,
            maxWebhooks=maxWebhooks,
            _configuration=_configuration,
            **kwargs,
        )
