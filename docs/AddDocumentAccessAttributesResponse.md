# AddDocumentAccessAttributesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Document Action message | [optional] 

## Example

```python
from formkiq_client.models.add_document_access_attributes_response import AddDocumentAccessAttributesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentAccessAttributesResponse from a JSON string
add_document_access_attributes_response_instance = AddDocumentAccessAttributesResponse.from_json(json)
# print the JSON string representation of the object
print(AddDocumentAccessAttributesResponse.to_json())

# convert the object into a dict
add_document_access_attributes_response_dict = add_document_access_attributes_response_instance.to_dict()
# create an instance of AddDocumentAccessAttributesResponse from a dict
add_document_access_attributes_response_form_dict = add_document_access_attributes_response.from_dict(add_document_access_attributes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


