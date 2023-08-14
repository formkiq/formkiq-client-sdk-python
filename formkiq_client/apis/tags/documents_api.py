# coding: utf-8

"""
    FormKiQ HTTP API

    Formkiq API: Document Management Platform API using JWT Authentication  # noqa: E501

    The version of the OpenAPI document: 1.12.0
    Contact: support@formkiq.com
    Generated by: https://openapi-generator.tech
"""

from formkiq_client.paths.documents.post import AddDocument
from formkiq_client.paths.documents_upload.post import AddDocumentUpload
from formkiq_client.paths.documents_compress.post import CompressDocuments
from formkiq_client.paths.documents_document_id.delete import DeleteDocument
from formkiq_client.paths.documents_document_id.get import GetDocument
from formkiq_client.paths.documents_document_id_content.get import GetDocumentContent
from formkiq_client.paths.documents_document_id_upload.get import GetDocumentIdUpload
from formkiq_client.paths.documents_document_id_syncs.get import GetDocumentSyncs
from formkiq_client.paths.documents_upload.get import GetDocumentUpload
from formkiq_client.paths.documents_document_id_url.get import GetDocumentUrl
from formkiq_client.paths.documents.get import GetDocuments
from formkiq_client.paths.documents_document_id.patch import UpdateDocument


class DocumentsApi(
    AddDocument,
    AddDocumentUpload,
    CompressDocuments,
    DeleteDocument,
    GetDocument,
    GetDocumentContent,
    GetDocumentIdUpload,
    GetDocumentSyncs,
    GetDocumentUpload,
    GetDocumentUrl,
    GetDocuments,
    UpdateDocument,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
