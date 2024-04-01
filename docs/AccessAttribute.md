# AccessAttribute

Document Access Attribute (requires either: stringValue, numberValue, booleanValue)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Attribute key | [optional] 
**string_value** | **str** | Attribute with string value | [optional] 
**number_value** | **float** | Attribute with number value | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 

## Example

```python
from formkiq_client.models.access_attribute import AccessAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of AccessAttribute from a JSON string
access_attribute_instance = AccessAttribute.from_json(json)
# print the JSON string representation of the object
print(AccessAttribute.to_json())

# convert the object into a dict
access_attribute_dict = access_attribute_instance.to_dict()
# create an instance of AccessAttribute from a dict
access_attribute_form_dict = access_attribute.from_dict(access_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


