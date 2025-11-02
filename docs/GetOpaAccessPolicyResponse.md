# GetOpaAccessPolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opa_policy** | **str** | OPA Policy in REGO format | [optional] 

## Example

```python
from openapi_client.models.get_opa_access_policy_response import GetOpaAccessPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpaAccessPolicyResponse from a JSON string
get_opa_access_policy_response_instance = GetOpaAccessPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(GetOpaAccessPolicyResponse.to_json())

# convert the object into a dict
get_opa_access_policy_response_dict = get_opa_access_policy_response_instance.to_dict()
# create an instance of GetOpaAccessPolicyResponse from a dict
get_opa_access_policy_response_from_dict = GetOpaAccessPolicyResponse.from_dict(get_opa_access_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


