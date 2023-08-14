from formkiq_client.paths.documents_document_id_ocr.get import ApiForget
from formkiq_client.paths.documents_document_id_ocr.put import ApiForput
from formkiq_client.paths.documents_document_id_ocr.post import ApiForpost
from formkiq_client.paths.documents_document_id_ocr.delete import ApiFordelete


class DocumentsDocumentIdOcr(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
