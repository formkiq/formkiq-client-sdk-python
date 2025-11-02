# SetOpaAccessPolicyItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_items** | [**List[OpaPolicyItem]**](OpaPolicyItem.md) | List of OPA policy items | 

## Example

```python
from openapi_client.models.set_opa_access_policy_items_request import SetOpaAccessPolicyItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetOpaAccessPolicyItemsRequest from a JSON string
set_opa_access_policy_items_request_instance = SetOpaAccessPolicyItemsRequest.from_json(json)
# print the JSON string representation of the object
print(SetOpaAccessPolicyItemsRequest.to_json())

# convert the object into a dict
set_opa_access_policy_items_request_dict = set_opa_access_policy_items_request_instance.to_dict()
# create an instance of SetOpaAccessPolicyItemsRequest from a dict
set_opa_access_policy_items_request_from_dict = SetOpaAccessPolicyItemsRequest.from_dict(set_opa_access_policy_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


