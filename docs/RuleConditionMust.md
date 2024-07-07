# RuleConditionMust


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**RuleConditionAttribute**](RuleConditionAttribute.md) |  | [optional] 
**criterion** | [**RuleConditionCriterion**](RuleConditionCriterion.md) |  | [optional] 
**field_name** | **str** | Rule field name (only required for FIELD criterion) | [optional] 
**value** | **str** | Rule condition value | [optional] 
**operation** | [**RuleConditionOperation**](RuleConditionOperation.md) |  | [optional] 

## Example

```python
from formkiq_client.models.rule_condition_must import RuleConditionMust

# TODO update the JSON string below
json = "{}"
# create an instance of RuleConditionMust from a JSON string
rule_condition_must_instance = RuleConditionMust.from_json(json)
# print the JSON string representation of the object
print(RuleConditionMust.to_json())

# convert the object into a dict
rule_condition_must_dict = rule_condition_must_instance.to_dict()
# create an instance of RuleConditionMust from a dict
rule_condition_must_from_dict = RuleConditionMust.from_dict(rule_condition_must_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


