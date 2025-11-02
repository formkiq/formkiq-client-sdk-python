# SetDocumentAttributesRequest

Set List of document attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[AddDocumentAttribute]**](AddDocumentAttribute.md) | List of document attributes | [optional] 

## Example

```python
from openapi_client.models.set_document_attributes_request import SetDocumentAttributesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDocumentAttributesRequest from a JSON string
set_document_attributes_request_instance = SetDocumentAttributesRequest.from_json(json)
# print the JSON string representation of the object
print(SetDocumentAttributesRequest.to_json())

# convert the object into a dict
set_document_attributes_request_dict = set_document_attributes_request_instance.to_dict()
# create an instance of SetDocumentAttributesRequest from a dict
set_document_attributes_request_from_dict = SetDocumentAttributesRequest.from_dict(set_document_attributes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


