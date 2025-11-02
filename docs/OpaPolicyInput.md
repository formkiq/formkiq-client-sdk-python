# OpaPolicyInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_method** | [**OpaPolicyInputMethod**](OpaPolicyInputMethod.md) |  | [optional] 
**resource** | [**OpaPolicyInputResource**](OpaPolicyInputResource.md) |  | [optional] 

## Example

```python
from openapi_client.models.opa_policy_input import OpaPolicyInput

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyInput from a JSON string
opa_policy_input_instance = OpaPolicyInput.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyInput.to_json())

# convert the object into a dict
opa_policy_input_dict = opa_policy_input_instance.to_dict()
# create an instance of OpaPolicyInput from a dict
opa_policy_input_from_dict = OpaPolicyInput.from_dict(opa_policy_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


