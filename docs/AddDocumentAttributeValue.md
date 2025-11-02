# AddDocumentAttributeValue

Document Attribute Value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_value** | **str** | Attribute with string value | [optional] 
**string_values** | **List[str]** | Attribute with string values | [optional] 
**number_value** | **float** | Attribute with number value | [optional] 
**number_values** | **List[float]** | Attribute with number values | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 

## Example

```python
from openapi_client.model.add_document_attribute_value import AddDocumentAttributeValue

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentAttributeValue from a JSON string
add_document_attribute_value_instance = AddDocumentAttributeValue.from_json(json)
# print the JSON string representation of the object
print(AddDocumentAttributeValue.to_json())

# convert the object into a dict
add_document_attribute_value_dict = add_document_attribute_value_instance.to_dict()
# create an instance of AddDocumentAttributeValue from a dict
add_document_attribute_value_from_dict = AddDocumentAttributeValue.from_dict(add_document_attribute_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


