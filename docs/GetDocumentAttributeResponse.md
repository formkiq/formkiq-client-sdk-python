# GetDocumentAttributeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**DocumentAttribute**](DocumentAttribute.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_document_attribute_response import GetDocumentAttributeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentAttributeResponse from a JSON string
get_document_attribute_response_instance = GetDocumentAttributeResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentAttributeResponse.to_json())

# convert the object into a dict
get_document_attribute_response_dict = get_document_attribute_response_instance.to_dict()
# create an instance of GetDocumentAttributeResponse from a dict
get_document_attribute_response_from_dict = GetDocumentAttributeResponse.from_dict(get_document_attribute_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


