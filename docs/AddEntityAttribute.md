# AddEntityAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Attribute key | [optional] 
**string_value** | **str** | Attribute with string value | [optional] 
**string_values** | **List[str]** | Attribute with string values | [optional] 
**number_value** | **float** | Attribute with number value | [optional] 
**number_values** | **List[float]** | Attribute with number values | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 

## Example

```python
from openapi_client.model.add_entity_attribute import AddEntityAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of AddEntityAttribute from a JSON string
add_entity_attribute_instance = AddEntityAttribute.from_json(json)
# print the JSON string representation of the object
print(AddEntityAttribute.to_json())

# convert the object into a dict
add_entity_attribute_dict = add_entity_attribute_instance.to_dict()
# create an instance of AddEntityAttribute from a dict
add_entity_attribute_from_dict = AddEntityAttribute.from_dict(add_entity_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


