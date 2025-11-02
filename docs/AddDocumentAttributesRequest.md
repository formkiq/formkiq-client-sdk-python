# AddDocumentAttributesRequest

Add List of document attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[AddDocumentAttribute]**](AddDocumentAttribute.md) | List of document attributes | [optional] 

## Example

```python
from openapi_client.models.add_document_attributes_request import AddDocumentAttributesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentAttributesRequest from a JSON string
add_document_attributes_request_instance = AddDocumentAttributesRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentAttributesRequest.to_json())

# convert the object into a dict
add_document_attributes_request_dict = add_document_attributes_request_instance.to_dict()
# create an instance of AddDocumentAttributesRequest from a dict
add_document_attributes_request_from_dict = AddDocumentAttributesRequest.from_dict(add_document_attributes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


