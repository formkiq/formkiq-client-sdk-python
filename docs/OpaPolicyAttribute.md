# OpaPolicyAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Attribute Key | [optional] 
**eq** | [**OpaPolicyAttributeEq**](OpaPolicyAttributeEq.md) |  | [optional] 
**gt** | [**OpaPolicyAttributeGt**](OpaPolicyAttributeGt.md) |  | [optional] 
**gte** | [**OpaPolicyAttributeGte**](OpaPolicyAttributeGte.md) |  | [optional] 
**lt** | [**OpaPolicyAttributeLt**](OpaPolicyAttributeLt.md) |  | [optional] 
**lte** | [**OpaPolicyAttributeLte**](OpaPolicyAttributeLte.md) |  | [optional] 
**neq** | [**OpaPolicyAttributeNeq**](OpaPolicyAttributeNeq.md) |  | [optional] 
**var_in** | [**OpaPolicyAttributeIn**](OpaPolicyAttributeIn.md) |  | [optional] 
**not_in** | [**OpaPolicyAttributeNotIn**](OpaPolicyAttributeNotIn.md) |  | [optional] 

## Example

```python
from openapi_client.model.opa_policy_attribute import OpaPolicyAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyAttribute from a JSON string
opa_policy_attribute_instance = OpaPolicyAttribute.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyAttribute.to_json())

# convert the object into a dict
opa_policy_attribute_dict = opa_policy_attribute_instance.to_dict()
# create an instance of OpaPolicyAttribute from a dict
opa_policy_attribute_from_dict = OpaPolicyAttribute.from_dict(opa_policy_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


