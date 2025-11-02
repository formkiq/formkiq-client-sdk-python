# OpaPolicyAttributeGte

Attribute greater than and equals to criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_value** | **float** | The value to compare the Attribute Key value to | [optional] 

## Example

```python
from openapi_client.model.opa_policy_attribute_gte import OpaPolicyAttributeGte

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyAttributeGte from a JSON string
opa_policy_attribute_gte_instance = OpaPolicyAttributeGte.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyAttributeGte.to_json())

# convert the object into a dict
opa_policy_attribute_gte_dict = opa_policy_attribute_gte_instance.to_dict()
# create an instance of OpaPolicyAttributeGte from a dict
opa_policy_attribute_gte_from_dict = OpaPolicyAttributeGte.from_dict(opa_policy_attribute_gte_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


