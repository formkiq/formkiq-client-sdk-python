# EntityAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Attribute key | [optional] 
**string_value** | **str** | Attribute with string value | [optional] 
**string_values** | **List[str]** | Attribute with string values | [optional] 
**number_value** | **float** | Attribute with number value | [optional] 
**number_values** | **List[float]** | Attribute with number values | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 
**value_type** | [**AttributeValueType**](AttributeValueType.md) |  | [optional] 

## Example

```python
from openapi_client.model.entity_attribute import EntityAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of EntityAttribute from a JSON string
entity_attribute_instance = EntityAttribute.from_json(json)
# print the JSON string representation of the object
print(EntityAttribute.to_json())

# convert the object into a dict
entity_attribute_dict = entity_attribute_instance.to_dict()
# create an instance of EntityAttribute from a dict
entity_attribute_from_dict = EntityAttribute.from_dict(entity_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


