# OpaPolicyAttributeLte

Attribute less than and equals to criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_value** | **float** | The value to compare the Attribute Key value to | [optional] 

## Example

```python
from openapi_client.model.opa_policy_attribute_lte import OpaPolicyAttributeLte

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyAttributeLte from a JSON string
opa_policy_attribute_lte_instance = OpaPolicyAttributeLte.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyAttributeLte.to_json())

# convert the object into a dict
opa_policy_attribute_lte_dict = opa_policy_attribute_lte_instance.to_dict()
# create an instance of OpaPolicyAttributeLte from a dict
opa_policy_attribute_lte_from_dict = OpaPolicyAttributeLte.from_dict(opa_policy_attribute_lte_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


