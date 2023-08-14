import typing_extensions

from formkiq_client.apis.tags import TagValues
from formkiq_client.apis.tags.advanced_document_search_api import AdvancedDocumentSearchApi
from formkiq_client.apis.tags.antivirus_api import AntivirusApi
from formkiq_client.apis.tags.custom_index_api import CustomIndexApi
from formkiq_client.apis.tags.tag_index_api import TagIndexApi
from formkiq_client.apis.tags.document_actions_api import DocumentActionsApi
from formkiq_client.apis.tags.document_ocr_api import DocumentOCRApi
from formkiq_client.apis.tags.document_search_api import DocumentSearchApi
from formkiq_client.apis.tags.document_shares_api import DocumentSharesApi
from formkiq_client.apis.tags.document_tags_api import DocumentTagsApi
from formkiq_client.apis.tags.document_versions_api import DocumentVersionsApi
from formkiq_client.apis.tags.documents_api import DocumentsApi
from formkiq_client.apis.tags.e_signature_api import ESignatureApi
from formkiq_client.apis.tags.folders_api import FoldersApi
from formkiq_client.apis.tags.onlyoffice_api import OnlyofficeApi
from formkiq_client.apis.tags.public_api import PublicApi
from formkiq_client.apis.tags.system_management_api import SystemManagementApi
from formkiq_client.apis.tags.tag_schema_api import TagSchemaApi
from formkiq_client.apis.tags.webhooks_api import WebhooksApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ADVANCED_DOCUMENT_SEARCH: AdvancedDocumentSearchApi,
        TagValues.ANTIVIRUS: AntivirusApi,
        TagValues.CUSTOM_INDEX: CustomIndexApi,
        TagValues.TAG_INDEX: TagIndexApi,
        TagValues.DOCUMENT_ACTIONS: DocumentActionsApi,
        TagValues.DOCUMENT_OCR: DocumentOCRApi,
        TagValues.DOCUMENT_SEARCH: DocumentSearchApi,
        TagValues.DOCUMENT_SHARES: DocumentSharesApi,
        TagValues.DOCUMENT_TAGS: DocumentTagsApi,
        TagValues.DOCUMENT_VERSIONS: DocumentVersionsApi,
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.ESIGNATURE: ESignatureApi,
        TagValues.FOLDERS: FoldersApi,
        TagValues.ONLYOFFICE: OnlyofficeApi,
        TagValues.PUBLIC: PublicApi,
        TagValues.SYSTEM_MANAGEMENT: SystemManagementApi,
        TagValues.TAG_SCHEMA: TagSchemaApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ADVANCED_DOCUMENT_SEARCH: AdvancedDocumentSearchApi,
        TagValues.ANTIVIRUS: AntivirusApi,
        TagValues.CUSTOM_INDEX: CustomIndexApi,
        TagValues.TAG_INDEX: TagIndexApi,
        TagValues.DOCUMENT_ACTIONS: DocumentActionsApi,
        TagValues.DOCUMENT_OCR: DocumentOCRApi,
        TagValues.DOCUMENT_SEARCH: DocumentSearchApi,
        TagValues.DOCUMENT_SHARES: DocumentSharesApi,
        TagValues.DOCUMENT_TAGS: DocumentTagsApi,
        TagValues.DOCUMENT_VERSIONS: DocumentVersionsApi,
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.ESIGNATURE: ESignatureApi,
        TagValues.FOLDERS: FoldersApi,
        TagValues.ONLYOFFICE: OnlyofficeApi,
        TagValues.PUBLIC: PublicApi,
        TagValues.SYSTEM_MANAGEMENT: SystemManagementApi,
        TagValues.TAG_SCHEMA: TagSchemaApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)
