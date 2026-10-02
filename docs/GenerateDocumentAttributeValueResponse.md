# GenerateDocumentAttributeValueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**DocumentAttribute**](DocumentAttribute.md) |  | 
**sequence** | **int** | Allocated sequence number | 
**period** | **str** | Sequence period used for the allocation | 

## Example

```python
from formkiq_client.models.generate_document_attribute_value_response import GenerateDocumentAttributeValueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateDocumentAttributeValueResponse from a JSON string
generate_document_attribute_value_response_instance = GenerateDocumentAttributeValueResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateDocumentAttributeValueResponse.to_json())

# convert the object into a dict
generate_document_attribute_value_response_dict = generate_document_attribute_value_response_instance.to_dict()
# create an instance of GenerateDocumentAttributeValueResponse from a dict
generate_document_attribute_value_response_from_dict = GenerateDocumentAttributeValueResponse.from_dict(generate_document_attribute_value_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


