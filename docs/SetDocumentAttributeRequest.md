# SetDocumentAttributeRequest

Set List of document attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**AddDocumentAttributeValue**](AddDocumentAttributeValue.md) |  | [optional] 

## Example

```python
from formkiq_client.models.set_document_attribute_request import SetDocumentAttributeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDocumentAttributeRequest from a JSON string
set_document_attribute_request_instance = SetDocumentAttributeRequest.from_json(json)
# print the JSON string representation of the object
print(SetDocumentAttributeRequest.to_json())

# convert the object into a dict
set_document_attribute_request_dict = set_document_attribute_request_instance.to_dict()
# create an instance of SetDocumentAttributeRequest from a dict
set_document_attribute_request_from_dict = SetDocumentAttributeRequest.from_dict(set_document_attribute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


