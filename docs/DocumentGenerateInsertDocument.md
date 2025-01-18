# DocumentGenerateInsertDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | [**DocumentGenerateInsertDocumentPosition**](DocumentGenerateInsertDocumentPosition.md) |  | 
**document_id** | **str** | Document Identifier of the data source document | 

## Example

```python
from formkiq_client.models.document_generate_insert_document import DocumentGenerateInsertDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentGenerateInsertDocument from a JSON string
document_generate_insert_document_instance = DocumentGenerateInsertDocument.from_json(json)
# print the JSON string representation of the object
print(DocumentGenerateInsertDocument.to_json())

# convert the object into a dict
document_generate_insert_document_dict = document_generate_insert_document_instance.to_dict()
# create an instance of DocumentGenerateInsertDocument from a dict
document_generate_insert_document_from_dict = DocumentGenerateInsertDocument.from_dict(document_generate_insert_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


