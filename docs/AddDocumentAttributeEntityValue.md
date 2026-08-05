# AddDocumentAttributeEntityValue

Document Entity Attribute Value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type_id** | **str** | EntityType Identifier or Entity Type Name | 
**entity_id** | **str** | Entity Identifier | 
**namespace** | [**EntityTypeNamespace**](EntityTypeNamespace.md) |  | [optional] 

## Example

```python
from formkiq_client.models.add_document_attribute_entity_value import AddDocumentAttributeEntityValue

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentAttributeEntityValue from a JSON string
add_document_attribute_entity_value_instance = AddDocumentAttributeEntityValue.from_json(json)
# print the JSON string representation of the object
print(AddDocumentAttributeEntityValue.to_json())

# convert the object into a dict
add_document_attribute_entity_value_dict = add_document_attribute_entity_value_instance.to_dict()
# create an instance of AddDocumentAttributeEntityValue from a dict
add_document_attribute_entity_value_from_dict = AddDocumentAttributeEntityValue.from_dict(add_document_attribute_entity_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


