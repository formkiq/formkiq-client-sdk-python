# OpaPolicyAttributeNotIn

Attribute Not In to criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_values** | **List[str]** | The value to compare the Attribute Key value to | [optional] 

## Example

```python
from formkiq_client.models.opa_policy_attribute_not_in import OpaPolicyAttributeNotIn

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyAttributeNotIn from a JSON string
opa_policy_attribute_not_in_instance = OpaPolicyAttributeNotIn.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyAttributeNotIn.to_json())

# convert the object into a dict
opa_policy_attribute_not_in_dict = opa_policy_attribute_not_in_instance.to_dict()
# create an instance of OpaPolicyAttributeNotIn from a dict
opa_policy_attribute_not_in_from_dict = OpaPolicyAttributeNotIn.from_dict(opa_policy_attribute_not_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


