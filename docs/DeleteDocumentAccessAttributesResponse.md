# DeleteDocumentAccessAttributesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Document Action message | [optional] 

## Example

```python
from formkiq_client.models.delete_document_access_attributes_response import DeleteDocumentAccessAttributesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDocumentAccessAttributesResponse from a JSON string
delete_document_access_attributes_response_instance = DeleteDocumentAccessAttributesResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteDocumentAccessAttributesResponse.to_json())

# convert the object into a dict
delete_document_access_attributes_response_dict = delete_document_access_attributes_response_instance.to_dict()
# create an instance of DeleteDocumentAccessAttributesResponse from a dict
delete_document_access_attributes_response_form_dict = delete_document_access_attributes_response.from_dict(delete_document_access_attributes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


