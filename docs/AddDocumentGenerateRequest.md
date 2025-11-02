# AddDocumentGenerateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | [**LocaleInfo**](LocaleInfo.md) |  | [optional] 
**insert_documents** | [**List[DocumentGenerateInsertDocument]**](DocumentGenerateInsertDocument.md) | List of documents to insert | [optional] 
**datasources** | [**List[DocumentGenerateDataSource]**](DocumentGenerateDataSource.md) | List of data sources | [optional] 
**output_type** | [**DocumentGenerateOutputType**](DocumentGenerateOutputType.md) |  | [optional] 
**save_as_document_id** | **str** | Save the generated document with a specific documentId | [optional] 
**path** | **str** | The path of the generated document | [optional] 

## Example

```python
from openapi_client.models.add_document_generate_request import AddDocumentGenerateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentGenerateRequest from a JSON string
add_document_generate_request_instance = AddDocumentGenerateRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentGenerateRequest.to_json())

# convert the object into a dict
add_document_generate_request_dict = add_document_generate_request_instance.to_dict()
# create an instance of AddDocumentGenerateRequest from a dict
add_document_generate_request_from_dict = AddDocumentGenerateRequest.from_dict(add_document_generate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


