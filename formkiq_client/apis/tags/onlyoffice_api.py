# coding: utf-8

"""
    FormKiQ HTTP API

    Formkiq API: Document Management Platform API using JWT Authentication  # noqa: E501

    The version of the OpenAPI document: 1.12.0
    Contact: support@formkiq.com
    Generated by: https://openapi-generator.tech
"""

from formkiq_client.paths.onlyoffice_document_id_edit.post import OnlyOfficeDocumentEdit
from formkiq_client.paths.onlyoffice_new.post import OnlyOfficeDocumentNew
from formkiq_client.paths.onlyoffice_document_id_save.post import OnlyOfficeDocumentSave


class OnlyofficeApi(
    OnlyOfficeDocumentEdit,
    OnlyOfficeDocumentNew,
    OnlyOfficeDocumentSave,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
