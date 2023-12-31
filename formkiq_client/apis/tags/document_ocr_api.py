# coding: utf-8

"""
    FormKiQ HTTP API

    Formkiq API: Document Management Platform API using JWT Authentication  # noqa: E501

    The version of the OpenAPI document: 1.12.0
    Contact: support@formkiq.com
    Generated by: https://openapi-generator.tech
"""

from formkiq_client.paths.documents_document_id_ocr.post import AddDocumentOcr
from formkiq_client.paths.documents_document_id_ocr.delete import DeleteDocumentOcr
from formkiq_client.paths.documents_document_id_ocr.get import GetDocumentOcr
from formkiq_client.paths.documents_document_id_ocr.put import SetDocumentOcr


class DocumentOCRApi(
    AddDocumentOcr,
    DeleteDocumentOcr,
    GetDocumentOcr,
    SetDocumentOcr,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
