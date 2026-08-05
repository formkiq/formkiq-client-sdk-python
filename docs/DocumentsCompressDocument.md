# DocumentsCompressDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document Identifier | 
**artifact_id** | **str** | Artifact Identifier | [optional] 

## Example

```python
from formkiq_client.models.documents_compress_document import DocumentsCompressDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsCompressDocument from a JSON string
documents_compress_document_instance = DocumentsCompressDocument.from_json(json)
# print the JSON string representation of the object
print(DocumentsCompressDocument.to_json())

# convert the object into a dict
documents_compress_document_dict = documents_compress_document_instance.to_dict()
# create an instance of DocumentsCompressDocument from a dict
documents_compress_document_from_dict = DocumentsCompressDocument.from_dict(documents_compress_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


