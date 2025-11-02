# OpaPolicyAttributeNeq

Attribute not equal to criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_value** | **str** | The value to compare the Attribute Key value to | [optional] 

## Example

```python
from openapi_client.model.opa_policy_attribute_neq import OpaPolicyAttributeNeq

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyAttributeNeq from a JSON string
opa_policy_attribute_neq_instance = OpaPolicyAttributeNeq.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyAttributeNeq.to_json())

# convert the object into a dict
opa_policy_attribute_neq_dict = opa_policy_attribute_neq_instance.to_dict()
# create an instance of OpaPolicyAttributeNeq from a dict
opa_policy_attribute_neq_from_dict = OpaPolicyAttributeNeq.from_dict(opa_policy_attribute_neq_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


