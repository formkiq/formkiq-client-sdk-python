import typing_extensions

from formkiq_client.paths import PathValues
from formkiq_client.apis.paths.version import Version
from formkiq_client.apis.paths.sites import Sites
from formkiq_client.apis.paths.configuration import Configuration
from formkiq_client.apis.paths.configuration_api_keys import ConfigurationApiKeys
from formkiq_client.apis.paths.configuration_api_keys_api_key import ConfigurationApiKeysApiKey
from formkiq_client.apis.paths.documents import Documents
from formkiq_client.apis.paths.documents_document_id import DocumentsDocumentId
from formkiq_client.apis.paths.documents_document_id_content import DocumentsDocumentIdContent
from formkiq_client.apis.paths.documents_document_id_tags import DocumentsDocumentIdTags
from formkiq_client.apis.paths.documents_document_id_tags_tag_key import DocumentsDocumentIdTagsTagKey
from formkiq_client.apis.paths.documents_document_id_tags_tag_key_tag_value import DocumentsDocumentIdTagsTagKeyTagValue
from formkiq_client.apis.paths.documents_tags import DocumentsTags
from formkiq_client.apis.paths.documents_document_id_url import DocumentsDocumentIdUrl
from formkiq_client.apis.paths.documents_upload import DocumentsUpload
from formkiq_client.apis.paths.documents_document_id_upload import DocumentsDocumentIdUpload
from formkiq_client.apis.paths.documents_compress import DocumentsCompress
from formkiq_client.apis.paths.search import Search
from formkiq_client.apis.paths.search_fulltext import SearchFulltext
from formkiq_client.apis.paths.query_fulltext import QueryFulltext
from formkiq_client.apis.paths.documents_document_id_actions import DocumentsDocumentIdActions
from formkiq_client.apis.paths.documents_document_id_ocr import DocumentsDocumentIdOcr
from formkiq_client.apis.paths.documents_document_id_versions import DocumentsDocumentIdVersions
from formkiq_client.apis.paths.documents_document_id_versions_version_key import DocumentsDocumentIdVersionsVersionKey
from formkiq_client.apis.paths.folders import Folders
from formkiq_client.apis.paths.folders_index_key import FoldersIndexKey
from formkiq_client.apis.paths.shares import Shares
from formkiq_client.apis.paths.shares_folders_index_key import SharesFoldersIndexKey
from formkiq_client.apis.paths.shares_share_key import SharesShareKey
from formkiq_client.apis.paths.tag_schemas import TagSchemas
from formkiq_client.apis.paths.tag_schemas_tag_schema_id import TagSchemasTagSchemaId
from formkiq_client.apis.paths.documents_document_id_antivirus import DocumentsDocumentIdAntivirus
from formkiq_client.apis.paths.documents_document_id_fulltext import DocumentsDocumentIdFulltext
from formkiq_client.apis.paths.documents_document_id_fulltext_tags_tag_key import DocumentsDocumentIdFulltextTagsTagKey
from formkiq_client.apis.paths.documents_document_id_fulltext_tags_tag_key_tag_value import DocumentsDocumentIdFulltextTagsTagKeyTagValue
from formkiq_client.apis.paths.documents_document_id_syncs import DocumentsDocumentIdSyncs
from formkiq_client.apis.paths.public_documents import PublicDocuments
from formkiq_client.apis.paths.public_webhooks_webhooks import PublicWebhooksWebhooks
from formkiq_client.apis.paths.private_webhooks_webhooks import PrivateWebhooksWebhooks
from formkiq_client.apis.paths.webhooks import Webhooks
from formkiq_client.apis.paths.webhooks_webhook_id import WebhooksWebhookId
from formkiq_client.apis.paths.webhooks_webhook_id_tags import WebhooksWebhookIdTags
from formkiq_client.apis.paths.onlyoffice_document_id_edit import OnlyofficeDocumentIdEdit
from formkiq_client.apis.paths.onlyoffice_new import OnlyofficeNew
from formkiq_client.apis.paths.onlyoffice_document_id_save import OnlyofficeDocumentIdSave
from formkiq_client.apis.paths.indices_index_type_move import IndicesIndexTypeMove
from formkiq_client.apis.paths.indices_index_type_index_key import IndicesIndexTypeIndexKey
from formkiq_client.apis.paths.indices_search import IndicesSearch
from formkiq_client.apis.paths.esignature_docusign_document_id import EsignatureDocusignDocumentId
from formkiq_client.apis.paths.esignature_docusign_config import EsignatureDocusignConfig
from formkiq_client.apis.paths.esignature_docusign_events import EsignatureDocusignEvents

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.VERSION: Version,
        PathValues.SITES: Sites,
        PathValues.CONFIGURATION: Configuration,
        PathValues.CONFIGURATION_API_KEYS: ConfigurationApiKeys,
        PathValues.CONFIGURATION_API_KEYS_API_KEY: ConfigurationApiKeysApiKey,
        PathValues.DOCUMENTS: Documents,
        PathValues.DOCUMENTS_DOCUMENT_ID: DocumentsDocumentId,
        PathValues.DOCUMENTS_DOCUMENT_ID_CONTENT: DocumentsDocumentIdContent,
        PathValues.DOCUMENTS_DOCUMENT_ID_TAGS: DocumentsDocumentIdTags,
        PathValues.DOCUMENTS_DOCUMENT_ID_TAGS_TAG_KEY: DocumentsDocumentIdTagsTagKey,
        PathValues.DOCUMENTS_DOCUMENT_ID_TAGS_TAG_KEY_TAG_VALUE: DocumentsDocumentIdTagsTagKeyTagValue,
        PathValues.DOCUMENTS_TAGS: DocumentsTags,
        PathValues.DOCUMENTS_DOCUMENT_ID_URL: DocumentsDocumentIdUrl,
        PathValues.DOCUMENTS_UPLOAD: DocumentsUpload,
        PathValues.DOCUMENTS_DOCUMENT_ID_UPLOAD: DocumentsDocumentIdUpload,
        PathValues.DOCUMENTS_COMPRESS: DocumentsCompress,
        PathValues.SEARCH: Search,
        PathValues.SEARCH_FULLTEXT: SearchFulltext,
        PathValues.QUERY_FULLTEXT: QueryFulltext,
        PathValues.DOCUMENTS_DOCUMENT_ID_ACTIONS: DocumentsDocumentIdActions,
        PathValues.DOCUMENTS_DOCUMENT_ID_OCR: DocumentsDocumentIdOcr,
        PathValues.DOCUMENTS_DOCUMENT_ID_VERSIONS: DocumentsDocumentIdVersions,
        PathValues.DOCUMENTS_DOCUMENT_ID_VERSIONS_VERSION_KEY: DocumentsDocumentIdVersionsVersionKey,
        PathValues.FOLDERS: Folders,
        PathValues.FOLDERS_INDEX_KEY: FoldersIndexKey,
        PathValues.SHARES: Shares,
        PathValues.SHARES_FOLDERS_INDEX_KEY: SharesFoldersIndexKey,
        PathValues.SHARES_SHARE_KEY: SharesShareKey,
        PathValues.TAG_SCHEMAS: TagSchemas,
        PathValues.TAG_SCHEMAS_TAG_SCHEMA_ID: TagSchemasTagSchemaId,
        PathValues.DOCUMENTS_DOCUMENT_ID_ANTIVIRUS: DocumentsDocumentIdAntivirus,
        PathValues.DOCUMENTS_DOCUMENT_ID_FULLTEXT: DocumentsDocumentIdFulltext,
        PathValues.DOCUMENTS_DOCUMENT_ID_FULLTEXT_TAGS_TAG_KEY: DocumentsDocumentIdFulltextTagsTagKey,
        PathValues.DOCUMENTS_DOCUMENT_ID_FULLTEXT_TAGS_TAG_KEY_TAG_VALUE: DocumentsDocumentIdFulltextTagsTagKeyTagValue,
        PathValues.DOCUMENTS_DOCUMENT_ID_SYNCS: DocumentsDocumentIdSyncs,
        PathValues.PUBLIC_DOCUMENTS: PublicDocuments,
        PathValues.PUBLIC_WEBHOOKS_WEBHOOKS: PublicWebhooksWebhooks,
        PathValues.PRIVATE_WEBHOOKS_WEBHOOKS: PrivateWebhooksWebhooks,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_WEBHOOK_ID: WebhooksWebhookId,
        PathValues.WEBHOOKS_WEBHOOK_ID_TAGS: WebhooksWebhookIdTags,
        PathValues.ONLYOFFICE_DOCUMENT_ID_EDIT: OnlyofficeDocumentIdEdit,
        PathValues.ONLYOFFICE_NEW: OnlyofficeNew,
        PathValues.ONLYOFFICE_DOCUMENT_ID_SAVE: OnlyofficeDocumentIdSave,
        PathValues.INDICES_INDEX_TYPE_MOVE: IndicesIndexTypeMove,
        PathValues.INDICES_INDEX_TYPE_INDEX_KEY: IndicesIndexTypeIndexKey,
        PathValues.INDICES_SEARCH: IndicesSearch,
        PathValues.ESIGNATURE_DOCUSIGN_DOCUMENT_ID: EsignatureDocusignDocumentId,
        PathValues.ESIGNATURE_DOCUSIGN_CONFIG: EsignatureDocusignConfig,
        PathValues.ESIGNATURE_DOCUSIGN_EVENTS: EsignatureDocusignEvents,
    }
)

path_to_api = PathToApi(
    {
        PathValues.VERSION: Version,
        PathValues.SITES: Sites,
        PathValues.CONFIGURATION: Configuration,
        PathValues.CONFIGURATION_API_KEYS: ConfigurationApiKeys,
        PathValues.CONFIGURATION_API_KEYS_API_KEY: ConfigurationApiKeysApiKey,
        PathValues.DOCUMENTS: Documents,
        PathValues.DOCUMENTS_DOCUMENT_ID: DocumentsDocumentId,
        PathValues.DOCUMENTS_DOCUMENT_ID_CONTENT: DocumentsDocumentIdContent,
        PathValues.DOCUMENTS_DOCUMENT_ID_TAGS: DocumentsDocumentIdTags,
        PathValues.DOCUMENTS_DOCUMENT_ID_TAGS_TAG_KEY: DocumentsDocumentIdTagsTagKey,
        PathValues.DOCUMENTS_DOCUMENT_ID_TAGS_TAG_KEY_TAG_VALUE: DocumentsDocumentIdTagsTagKeyTagValue,
        PathValues.DOCUMENTS_TAGS: DocumentsTags,
        PathValues.DOCUMENTS_DOCUMENT_ID_URL: DocumentsDocumentIdUrl,
        PathValues.DOCUMENTS_UPLOAD: DocumentsUpload,
        PathValues.DOCUMENTS_DOCUMENT_ID_UPLOAD: DocumentsDocumentIdUpload,
        PathValues.DOCUMENTS_COMPRESS: DocumentsCompress,
        PathValues.SEARCH: Search,
        PathValues.SEARCH_FULLTEXT: SearchFulltext,
        PathValues.QUERY_FULLTEXT: QueryFulltext,
        PathValues.DOCUMENTS_DOCUMENT_ID_ACTIONS: DocumentsDocumentIdActions,
        PathValues.DOCUMENTS_DOCUMENT_ID_OCR: DocumentsDocumentIdOcr,
        PathValues.DOCUMENTS_DOCUMENT_ID_VERSIONS: DocumentsDocumentIdVersions,
        PathValues.DOCUMENTS_DOCUMENT_ID_VERSIONS_VERSION_KEY: DocumentsDocumentIdVersionsVersionKey,
        PathValues.FOLDERS: Folders,
        PathValues.FOLDERS_INDEX_KEY: FoldersIndexKey,
        PathValues.SHARES: Shares,
        PathValues.SHARES_FOLDERS_INDEX_KEY: SharesFoldersIndexKey,
        PathValues.SHARES_SHARE_KEY: SharesShareKey,
        PathValues.TAG_SCHEMAS: TagSchemas,
        PathValues.TAG_SCHEMAS_TAG_SCHEMA_ID: TagSchemasTagSchemaId,
        PathValues.DOCUMENTS_DOCUMENT_ID_ANTIVIRUS: DocumentsDocumentIdAntivirus,
        PathValues.DOCUMENTS_DOCUMENT_ID_FULLTEXT: DocumentsDocumentIdFulltext,
        PathValues.DOCUMENTS_DOCUMENT_ID_FULLTEXT_TAGS_TAG_KEY: DocumentsDocumentIdFulltextTagsTagKey,
        PathValues.DOCUMENTS_DOCUMENT_ID_FULLTEXT_TAGS_TAG_KEY_TAG_VALUE: DocumentsDocumentIdFulltextTagsTagKeyTagValue,
        PathValues.DOCUMENTS_DOCUMENT_ID_SYNCS: DocumentsDocumentIdSyncs,
        PathValues.PUBLIC_DOCUMENTS: PublicDocuments,
        PathValues.PUBLIC_WEBHOOKS_WEBHOOKS: PublicWebhooksWebhooks,
        PathValues.PRIVATE_WEBHOOKS_WEBHOOKS: PrivateWebhooksWebhooks,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_WEBHOOK_ID: WebhooksWebhookId,
        PathValues.WEBHOOKS_WEBHOOK_ID_TAGS: WebhooksWebhookIdTags,
        PathValues.ONLYOFFICE_DOCUMENT_ID_EDIT: OnlyofficeDocumentIdEdit,
        PathValues.ONLYOFFICE_NEW: OnlyofficeNew,
        PathValues.ONLYOFFICE_DOCUMENT_ID_SAVE: OnlyofficeDocumentIdSave,
        PathValues.INDICES_INDEX_TYPE_MOVE: IndicesIndexTypeMove,
        PathValues.INDICES_INDEX_TYPE_INDEX_KEY: IndicesIndexTypeIndexKey,
        PathValues.INDICES_SEARCH: IndicesSearch,
        PathValues.ESIGNATURE_DOCUSIGN_DOCUMENT_ID: EsignatureDocusignDocumentId,
        PathValues.ESIGNATURE_DOCUSIGN_CONFIG: EsignatureDocusignConfig,
        PathValues.ESIGNATURE_DOCUSIGN_EVENTS: EsignatureDocusignEvents,
    }
)
