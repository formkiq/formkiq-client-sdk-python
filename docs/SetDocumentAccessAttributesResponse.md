# SetDocumentAccessAttributesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Document Action message | [optional] 

## Example

```python
from formkiq_client.models.set_document_access_attributes_response import SetDocumentAccessAttributesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetDocumentAccessAttributesResponse from a JSON string
set_document_access_attributes_response_instance = SetDocumentAccessAttributesResponse.from_json(json)
# print the JSON string representation of the object
print(SetDocumentAccessAttributesResponse.to_json())

# convert the object into a dict
set_document_access_attributes_response_dict = set_document_access_attributes_response_instance.to_dict()
# create an instance of SetDocumentAccessAttributesResponse from a dict
set_document_access_attributes_response_form_dict = set_document_access_attributes_response.from_dict(set_document_access_attributes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


