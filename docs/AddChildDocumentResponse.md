# AddChildDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document Identifier | [optional] 
**upload_url** | **str** | Url to upload document to | [optional] 

## Example

```python
from formkiq_client.models.add_child_document_response import AddChildDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddChildDocumentResponse from a JSON string
add_child_document_response_instance = AddChildDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(AddChildDocumentResponse.to_json())

# convert the object into a dict
add_child_document_response_dict = add_child_document_response_instance.to_dict()
# create an instance of AddChildDocumentResponse from a dict
add_child_document_response_from_dict = AddChildDocumentResponse.from_dict(add_child_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


