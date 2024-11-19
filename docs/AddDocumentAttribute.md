# AddDocumentAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Attribute key | 
**string_value** | **str** | Attribute with string value | [optional] 
**string_values** | **List[str]** | Attribute with string values | [optional] 
**number_value** | **float** | Attribute with number value | [optional] 
**number_values** | **List[float]** | Attribute with number values | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 
**classification_id** | **str** | Classification Identifier | 
**document_id** | **str** | Relationship To Document Identifier | 
**relationship** | [**DocumentRelationshipType**](DocumentRelationshipType.md) |  | 
**inverse_relationship** | [**DocumentRelationshipType**](DocumentRelationshipType.md) |  | [optional] 

## Example

```python
from formkiq_client.models.add_document_attribute import AddDocumentAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentAttribute from a JSON string
add_document_attribute_instance = AddDocumentAttribute.from_json(json)
# print the JSON string representation of the object
print(AddDocumentAttribute.to_json())

# convert the object into a dict
add_document_attribute_dict = add_document_attribute_instance.to_dict()
# create an instance of AddDocumentAttribute from a dict
add_document_attribute_from_dict = AddDocumentAttribute.from_dict(add_document_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


