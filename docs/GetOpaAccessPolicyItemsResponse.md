# GetOpaAccessPolicyItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_items** | [**List[OpaPolicyItem]**](OpaPolicyItem.md) |  | [optional] 

## Example

```python
from openapi_client.model.get_opa_access_policy_items_response import GetOpaAccessPolicyItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpaAccessPolicyItemsResponse from a JSON string
get_opa_access_policy_items_response_instance = GetOpaAccessPolicyItemsResponse.from_json(json)
# print the JSON string representation of the object
print(GetOpaAccessPolicyItemsResponse.to_json())

# convert the object into a dict
get_opa_access_policy_items_response_dict = get_opa_access_policy_items_response_instance.to_dict()
# create an instance of GetOpaAccessPolicyItemsResponse from a dict
get_opa_access_policy_items_response_from_dict = GetOpaAccessPolicyItemsResponse.from_dict(get_opa_access_policy_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


