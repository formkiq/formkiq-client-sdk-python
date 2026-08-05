# AddDocumentAttributeEntities

Document Entity Attribute with multiple values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Attribute key | 
**entities** | [**List[AddDocumentAttributeEntityValue]**](AddDocumentAttributeEntityValue.md) | Attribute with entity values | 

## Example

```python
from formkiq_client.models.add_document_attribute_entities import AddDocumentAttributeEntities

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentAttributeEntities from a JSON string
add_document_attribute_entities_instance = AddDocumentAttributeEntities.from_json(json)
# print the JSON string representation of the object
print(AddDocumentAttributeEntities.to_json())

# convert the object into a dict
add_document_attribute_entities_dict = add_document_attribute_entities_instance.to_dict()
# create an instance of AddDocumentAttributeEntities from a dict
add_document_attribute_entities_from_dict = AddDocumentAttributeEntities.from_dict(add_document_attribute_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


