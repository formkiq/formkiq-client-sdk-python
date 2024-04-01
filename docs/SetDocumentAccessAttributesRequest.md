# SetDocumentAccessAttributesRequest

List of document access attributes to set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_attributes** | [**List[AddAccessAttribute]**](AddAccessAttribute.md) | List of document access attributes | [optional] 

## Example

```python
from formkiq_client.models.set_document_access_attributes_request import SetDocumentAccessAttributesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDocumentAccessAttributesRequest from a JSON string
set_document_access_attributes_request_instance = SetDocumentAccessAttributesRequest.from_json(json)
# print the JSON string representation of the object
print(SetDocumentAccessAttributesRequest.to_json())

# convert the object into a dict
set_document_access_attributes_request_dict = set_document_access_attributes_request_instance.to_dict()
# create an instance of SetDocumentAccessAttributesRequest from a dict
set_document_access_attributes_request_form_dict = set_document_access_attributes_request.from_dict(set_document_access_attributes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


