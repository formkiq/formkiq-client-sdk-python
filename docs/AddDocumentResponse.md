# AddDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document Identifier | [optional] 
**site_id** | **str** | Site Identifier | [optional] 
**upload_url** | **str** | Url to upload document to | [optional] 
**headers** | **Dict[str, object]** |  | [optional] 
**documents** | [**List[AddChildDocumentResponse]**](AddChildDocumentResponse.md) | List of child documents | [optional] 

## Example

```python
from openapi_client.model.add_document_response import AddDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentResponse from a JSON string
add_document_response_instance = AddDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(AddDocumentResponse.to_json())

# convert the object into a dict
add_document_response_dict = add_document_response_instance.to_dict()
# create an instance of AddDocumentResponse from a dict
add_document_response_from_dict = AddDocumentResponse.from_dict(add_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


