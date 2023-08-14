# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from formkiq_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ADVANCED_DOCUMENT_SEARCH = "Advanced Document Search"
    ANTIVIRUS = "Antivirus"
    CUSTOM_INDEX = "Custom Index"
    TAG_INDEX = "Tag Index"
    DOCUMENT_ACTIONS = "Document Actions"
    DOCUMENT_OCR = "Document OCR"
    DOCUMENT_SEARCH = "Document Search"
    DOCUMENT_SHARES = "Document Shares"
    DOCUMENT_TAGS = "Document Tags"
    DOCUMENT_VERSIONS = "Document Versions"
    DOCUMENTS = "Documents"
    ESIGNATURE = "E-Signature"
    FOLDERS = "Folders"
    ONLYOFFICE = "Onlyoffice"
    PUBLIC = "Public"
    SYSTEM_MANAGEMENT = "System Management"
    TAG_SCHEMA = "Tag Schema"
    WEBHOOKS = "Webhooks"
