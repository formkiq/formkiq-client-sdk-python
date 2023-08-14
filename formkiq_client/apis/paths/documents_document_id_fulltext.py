from formkiq_client.paths.documents_document_id_fulltext.get import ApiForget
from formkiq_client.paths.documents_document_id_fulltext.put import ApiForput
from formkiq_client.paths.documents_document_id_fulltext.delete import ApiFordelete
from formkiq_client.paths.documents_document_id_fulltext.patch import ApiForpatch


class DocumentsDocumentIdFulltext(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
