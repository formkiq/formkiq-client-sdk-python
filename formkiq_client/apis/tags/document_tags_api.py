# coding: utf-8

"""
    FormKiQ HTTP API

    Formkiq API: Document Management Platform API using JWT Authentication  # noqa: E501

    The version of the OpenAPI document: 1.12.0
    Contact: support@formkiq.com
    Generated by: https://openapi-generator.tech
"""

from formkiq_client.paths.documents_document_id_tags.post import AddDocumentTags
from formkiq_client.paths.documents_document_id_tags_tag_key.delete import DeleteDocumentTag
from formkiq_client.paths.documents_document_id_tags_tag_key_tag_value.delete import DeleteDocumentTagAndValue
from formkiq_client.paths.documents_document_id_tags_tag_key.get import GetDocumentTag
from formkiq_client.paths.documents_document_id_tags.get import GetDocumentTags
from formkiq_client.paths.documents_document_id_tags_tag_key.put import SetDocumentTag
from formkiq_client.paths.documents_document_id_tags.put import SetDocumentTags
from formkiq_client.paths.documents_document_id_tags.patch import UpdateDocumentTags
from formkiq_client.paths.documents_tags.patch import UpdateMatchingDocumentTags


class DocumentTagsApi(
    AddDocumentTags,
    DeleteDocumentTag,
    DeleteDocumentTagAndValue,
    GetDocumentTag,
    GetDocumentTags,
    SetDocumentTag,
    SetDocumentTags,
    UpdateDocumentTags,
    UpdateMatchingDocumentTags,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass