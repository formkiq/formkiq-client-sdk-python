# OpaPolicyTestCriteriaGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | [**List[OpaPolicyTestCriterion]**](OpaPolicyTestCriterion.md) | AND criteria within this group. Groups are combined using OR. | 

## Example

```python
from formkiq_client.models.opa_policy_test_criteria_group import OpaPolicyTestCriteriaGroup

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyTestCriteriaGroup from a JSON string
opa_policy_test_criteria_group_instance = OpaPolicyTestCriteriaGroup.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyTestCriteriaGroup.to_json())

# convert the object into a dict
opa_policy_test_criteria_group_dict = opa_policy_test_criteria_group_instance.to_dict()
# create an instance of OpaPolicyTestCriteriaGroup from a dict
opa_policy_test_criteria_group_from_dict = OpaPolicyTestCriteriaGroup.from_dict(opa_policy_test_criteria_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


