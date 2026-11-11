# TestOpaAccessPolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision** | [**OpaPolicyTestDecision**](OpaPolicyTestDecision.md) |  | 
**criteria_groups** | [**List[OpaPolicyTestCriteriaGroup]**](OpaPolicyTestCriteriaGroup.md) | OR groups containing AND document criteria returned by partial evaluation. Empty when decision is ALLOW or DENY. | 

## Example

```python
from formkiq_client.models.test_opa_access_policy_response import TestOpaAccessPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestOpaAccessPolicyResponse from a JSON string
test_opa_access_policy_response_instance = TestOpaAccessPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(TestOpaAccessPolicyResponse.to_json())

# convert the object into a dict
test_opa_access_policy_response_dict = test_opa_access_policy_response_instance.to_dict()
# create an instance of TestOpaAccessPolicyResponse from a dict
test_opa_access_policy_response_from_dict = TestOpaAccessPolicyResponse.from_dict(test_opa_access_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


