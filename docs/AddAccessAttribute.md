# AddAccessAttribute

Document Access Attribute (requires either: stringValue, numberValue, booleanValue)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Attribute key | 
**string_value** | **str** | Attribute with string value | [optional] 
**number_value** | **float** | Attribute with number value | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 

## Example

```python
from formkiq_client.models.add_access_attribute import AddAccessAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of AddAccessAttribute from a JSON string
add_access_attribute_instance = AddAccessAttribute.from_json(json)
# print the JSON string representation of the object
print(AddAccessAttribute.to_json())

# convert the object into a dict
add_access_attribute_dict = add_access_attribute_instance.to_dict()
# create an instance of AddAccessAttribute from a dict
add_access_attribute_form_dict = add_access_attribute.from_dict(add_access_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


