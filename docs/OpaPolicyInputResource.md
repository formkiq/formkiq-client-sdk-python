# OpaPolicyInputResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_in** | **List[str]** | List of Resources | [optional] 
**not_in** | **List[str]** | List of Resources | [optional] 

## Example

```python
from formkiq_client.models.opa_policy_input_resource import OpaPolicyInputResource

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyInputResource from a JSON string
opa_policy_input_resource_instance = OpaPolicyInputResource.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyInputResource.to_json())

# convert the object into a dict
opa_policy_input_resource_dict = opa_policy_input_resource_instance.to_dict()
# create an instance of OpaPolicyInputResource from a dict
opa_policy_input_resource_from_dict = OpaPolicyInputResource.from_dict(opa_policy_input_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


