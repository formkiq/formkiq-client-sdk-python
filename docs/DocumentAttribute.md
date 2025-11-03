# DocumentAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Attribute key | [optional] 
**string_value** | **str** | Attribute with string value | [optional] 
**string_values** | **List[str]** | Attribute with string values | [optional] 
**number_value** | **float** | Attribute with number value | [optional] 
**number_values** | **List[float]** | Attribute with number values | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**user_id** | **str** | User who added attribute | [optional] 
**value_type** | [**AttributeValueType**](AttributeValueType.md) |  | [optional] 

## Example

```python
from formkiq_client.models.document_attribute import DocumentAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAttribute from a JSON string
document_attribute_instance = DocumentAttribute.from_json(json)
# print the JSON string representation of the object
print(DocumentAttribute.to_json())

# convert the object into a dict
document_attribute_dict = document_attribute_instance.to_dict()
# create an instance of DocumentAttribute from a dict
document_attribute_from_dict = DocumentAttribute.from_dict(document_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


