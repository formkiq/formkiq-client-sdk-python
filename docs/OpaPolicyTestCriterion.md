# OpaPolicyTestCriterion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Document attribute key referenced by the partial criterion. | 
**operator** | [**OpaPolicyTestOperator**](OpaPolicyTestOperator.md) |  | 
**value** | **object** | String, number, boolean, array, or null value used by the criterion. | 

## Example

```python
from formkiq_client.models.opa_policy_test_criterion import OpaPolicyTestCriterion

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyTestCriterion from a JSON string
opa_policy_test_criterion_instance = OpaPolicyTestCriterion.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyTestCriterion.to_json())

# convert the object into a dict
opa_policy_test_criterion_dict = opa_policy_test_criterion_instance.to_dict()
# create an instance of OpaPolicyTestCriterion from a dict
opa_policy_test_criterion_from_dict = OpaPolicyTestCriterion.from_dict(opa_policy_test_criterion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


