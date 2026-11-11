# AddDocumentAttributeValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_value** | **Dict[str, object]** | One JSON object stored as a single attribute value. Arrays, scalars, and null are not accepted at the top level. Nested values may include objects, arrays, strings, numbers, booleans, and null. Empty objects and nested empty arrays are accepted. Object property order and original number formatting are not preserved.  The complete stored DynamoDB item, including metadata and attribute names, must fit within 400 KB. Stored document nesting must not exceed 32 levels, including the wrapper. Numbers must fit within DynamoDB&#39;s supported range and 38 digits of precision. | [optional] 
**string_value** | **str** | Attribute with string value | [optional] 
**string_values** | **List[str]** | Attribute with string values | [optional] 
**number_value** | **float** | Attribute with number value | [optional] 
**number_values** | **List[float]** | Attribute with number values | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 
**date_value** | **str** | Attribute with date value | [optional] 
**date_values** | **List[str]** | Attribute with date values | [optional] 

## Example

```python
from formkiq_client.models.add_document_attribute_value import AddDocumentAttributeValue

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


