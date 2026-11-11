# OpaPolicyTestInputUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Simulated username placed at input.user.username. | 
**roles** | **List[str]** | Simulated roles placed at input.user.roles. Defaults to an empty array. | [optional] 
**claims** | **Dict[str, object]** | JSON-compatible simulated claims placed at input.user.claims. Defaults to an empty object. | [optional] 

## Example

```python
from formkiq_client.models.opa_policy_test_input_user import OpaPolicyTestInputUser

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyTestInputUser from a JSON string
opa_policy_test_input_user_instance = OpaPolicyTestInputUser.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyTestInputUser.to_json())

# convert the object into a dict
opa_policy_test_input_user_dict = opa_policy_test_input_user_instance.to_dict()
# create an instance of OpaPolicyTestInputUser from a dict
opa_policy_test_input_user_from_dict = OpaPolicyTestInputUser.from_dict(opa_policy_test_input_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


