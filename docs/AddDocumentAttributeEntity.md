# AddDocumentAttributeEntity

Document Entity Attribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Attribute key | 
**entity_type_id** | **str** | EntityType Identifier or Entity Type Name | 
**entity_id** | **str** | Entity Identifier | 
**namespace** | [**EntityTypeNamespace**](EntityTypeNamespace.md) |  | [optional] 

## Example

```python
from openapi_client.model.add_document_attribute_entity import AddDocumentAttributeEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentAttributeEntity from a JSON string
add_document_attribute_entity_instance = AddDocumentAttributeEntity.from_json(json)
# print the JSON string representation of the object
print(AddDocumentAttributeEntity.to_json())

# convert the object into a dict
add_document_attribute_entity_dict = add_document_attribute_entity_instance.to_dict()
# create an instance of AddDocumentAttributeEntity from a dict
add_document_attribute_entity_from_dict = AddDocumentAttributeEntity.from_dict(add_document_attribute_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


