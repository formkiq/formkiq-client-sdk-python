# OpaPolicyInputMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_in** | **List[str]** | List of HTTP Methods | [optional] 
**not_in** | **List[str]** | List of HTTP Methods | [optional] 

## Example

```python
from openapi_client.model.opa_policy_input_method import OpaPolicyInputMethod

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyInputMethod from a JSON string
opa_policy_input_method_instance = OpaPolicyInputMethod.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyInputMethod.to_json())

# convert the object into a dict
opa_policy_input_method_dict = opa_policy_input_method_instance.to_dict()
# create an instance of OpaPolicyInputMethod from a dict
opa_policy_input_method_from_dict = OpaPolicyInputMethod.from_dict(opa_policy_input_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


