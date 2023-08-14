from formkiq_client.paths.documents_document_id.get import ApiForget
from formkiq_client.paths.documents_document_id.delete import ApiFordelete
from formkiq_client.paths.documents_document_id.patch import ApiForpatch


class DocumentsDocumentId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
