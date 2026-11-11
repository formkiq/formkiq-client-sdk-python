# TestOpaAccessPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_items** | [**List[OpaPolicyItem]**](OpaPolicyItem.md) | Draft OPA policy items to test without persisting them. When omitted, the site&#39;s saved OPA access policy is tested. An explicitly empty array tests the generated deny-all policy. | [optional] 
**input** | [**OpaPolicyTestInput**](OpaPolicyTestInput.md) |  | 

## Example

```python
from formkiq_client.models.test_opa_access_policy_request import TestOpaAccessPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestOpaAccessPolicyRequest from a JSON string
test_opa_access_policy_request_instance = TestOpaAccessPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(TestOpaAccessPolicyRequest.to_json())

# convert the object into a dict
test_opa_access_policy_request_dict = test_opa_access_policy_request_instance.to_dict()
# create an instance of TestOpaAccessPolicyRequest from a dict
test_opa_access_policy_request_from_dict = TestOpaAccessPolicyRequest.from_dict(test_opa_access_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


