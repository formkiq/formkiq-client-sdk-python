# GetOpaAccessPoliciesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**opa_policies** | [**List[OpaPolicy]**](OpaPolicy.md) | List of OPA policies | [optional] 

## Example

```python
from formkiq_client.models.get_opa_access_policies_response import GetOpaAccessPoliciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpaAccessPoliciesResponse from a JSON string
get_opa_access_policies_response_instance = GetOpaAccessPoliciesResponse.from_json(json)
# print the JSON string representation of the object
print(GetOpaAccessPoliciesResponse.to_json())

# convert the object into a dict
get_opa_access_policies_response_dict = get_opa_access_policies_response_instance.to_dict()
# create an instance of GetOpaAccessPoliciesResponse from a dict
get_opa_access_policies_response_from_dict = GetOpaAccessPoliciesResponse.from_dict(get_opa_access_policies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


