# OpaPolicyAttributeEq

Attribute EQ criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_value** | **str** | The value to compare the Attribute Key value to | [optional] 
**number_value** | **float** | The value to compare the Attribute Key value to | [optional] 
**boolean_value** | **bool** | The value to compare the Attribute Key value to | [optional] 
**input** | [**OpaPolicyAttributeInput**](OpaPolicyAttributeInput.md) |  | [optional] 

## Example

```python
from openapi_client.models.opa_policy_attribute_eq import OpaPolicyAttributeEq

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyAttributeEq from a JSON string
opa_policy_attribute_eq_instance = OpaPolicyAttributeEq.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyAttributeEq.to_json())

# convert the object into a dict
opa_policy_attribute_eq_dict = opa_policy_attribute_eq_instance.to_dict()
# create an instance of OpaPolicyAttributeEq from a dict
opa_policy_attribute_eq_from_dict = OpaPolicyAttributeEq.from_dict(opa_policy_attribute_eq_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


