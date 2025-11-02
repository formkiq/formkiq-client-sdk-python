# OpaPolicyAttributeIn

Attribute In to criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_values** | **List[str]** | The value to compare the Attribute Key value to | [optional] 

## Example

```python
from openapi_client.model.opa_policy_attribute_in import OpaPolicyAttributeIn

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyAttributeIn from a JSON string
opa_policy_attribute_in_instance = OpaPolicyAttributeIn.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyAttributeIn.to_json())

# convert the object into a dict
opa_policy_attribute_in_dict = opa_policy_attribute_in_instance.to_dict()
# create an instance of OpaPolicyAttributeIn from a dict
opa_policy_attribute_in_from_dict = OpaPolicyAttributeIn.from_dict(opa_policy_attribute_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


