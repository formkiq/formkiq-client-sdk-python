# AddDocumentAttributeStandard

Document Attribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Attribute key | 
**string_value** | **str** | Attribute with string value | [optional] 
**string_values** | **List[str]** | Attribute with string values | [optional] 
**number_value** | **float** | Attribute with number value | [optional] 
**number_values** | **List[float]** | Attribute with number values | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 

## Example

```python
from formkiq_client.models.add_document_attribute_standard import AddDocumentAttributeStandard

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentAttributeStandard from a JSON string
add_document_attribute_standard_instance = AddDocumentAttributeStandard.from_json(json)
# print the JSON string representation of the object
print(AddDocumentAttributeStandard.to_json())

# convert the object into a dict
add_document_attribute_standard_dict = add_document_attribute_standard_instance.to_dict()
# create an instance of AddDocumentAttributeStandard from a dict
add_document_attribute_standard_from_dict = AddDocumentAttributeStandard.from_dict(add_document_attribute_standard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


