# AddDocumentAttributeRelationship

Document Relationship

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Relationship To Document Identifier | 
**relationship** | [**DocumentRelationshipType**](DocumentRelationshipType.md) |  | 
**inverse_relationship** | [**DocumentRelationshipType**](DocumentRelationshipType.md) |  | [optional] 

## Example

```python
from openapi_client.models.add_document_attribute_relationship import AddDocumentAttributeRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentAttributeRelationship from a JSON string
add_document_attribute_relationship_instance = AddDocumentAttributeRelationship.from_json(json)
# print the JSON string representation of the object
print(AddDocumentAttributeRelationship.to_json())

# convert the object into a dict
add_document_attribute_relationship_dict = add_document_attribute_relationship_instance.to_dict()
# create an instance of AddDocumentAttributeRelationship from a dict
add_document_attribute_relationship_from_dict = AddDocumentAttributeRelationship.from_dict(add_document_attribute_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


