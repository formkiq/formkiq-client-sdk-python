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


class GetDocumentFulltextResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            siteId = schemas.StrSchema
            content = schemas.StrSchema
            contentType = schemas.StrSchema
            path = schemas.StrSchema
            insertedDate = schemas.StrSchema
            documentId = schemas.StrSchema
            createdBy = schemas.StrSchema
            contentLength = schemas.IntSchema
            tags = schemas.DictSchema
            metadata = schemas.DictSchema
            __annotations__ = {
                "siteId": siteId,
                "content": content,
                "contentType": contentType,
                "path": path,
                "insertedDate": insertedDate,
                "documentId": documentId,
                "createdBy": createdBy,
                "contentLength": contentLength,
                "tags": tags,
                "metadata": metadata,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["siteId"]) -> MetaOapg.properties.siteId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentType"]) -> MetaOapg.properties.contentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["insertedDate"]) -> MetaOapg.properties.insertedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentId"]) -> MetaOapg.properties.documentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdBy"]) -> MetaOapg.properties.createdBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentLength"]) -> MetaOapg.properties.contentLength: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["siteId", "content", "contentType", "path", "insertedDate", "documentId", "createdBy", "contentLength", "tags", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["siteId"]) -> typing.Union[MetaOapg.properties.siteId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content"]) -> typing.Union[MetaOapg.properties.content, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentType"]) -> typing.Union[MetaOapg.properties.contentType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["insertedDate"]) -> typing.Union[MetaOapg.properties.insertedDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentId"]) -> typing.Union[MetaOapg.properties.documentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdBy"]) -> typing.Union[MetaOapg.properties.createdBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentLength"]) -> typing.Union[MetaOapg.properties.contentLength, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["siteId", "content", "contentType", "path", "insertedDate", "documentId", "createdBy", "contentLength", "tags", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        siteId: typing.Union[MetaOapg.properties.siteId, str, schemas.Unset] = schemas.unset,
        content: typing.Union[MetaOapg.properties.content, str, schemas.Unset] = schemas.unset,
        contentType: typing.Union[MetaOapg.properties.contentType, str, schemas.Unset] = schemas.unset,
        path: typing.Union[MetaOapg.properties.path, str, schemas.Unset] = schemas.unset,
        insertedDate: typing.Union[MetaOapg.properties.insertedDate, str, schemas.Unset] = schemas.unset,
        documentId: typing.Union[MetaOapg.properties.documentId, str, schemas.Unset] = schemas.unset,
        createdBy: typing.Union[MetaOapg.properties.createdBy, str, schemas.Unset] = schemas.unset,
        contentLength: typing.Union[MetaOapg.properties.contentLength, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tags: typing.Union[MetaOapg.properties.tags, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetDocumentFulltextResponse':
        return super().__new__(
            cls,
            *_args,
            siteId=siteId,
            content=content,
            contentType=contentType,
            path=path,
            insertedDate=insertedDate,
            documentId=documentId,
            createdBy=createdBy,
            contentLength=contentLength,
            tags=tags,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )