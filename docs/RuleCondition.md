# RuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**must** | [**List[RuleConditionMust]**](RuleConditionMust.md) | List of rule conditions | [optional] 

## Example

```python
from formkiq_client.models.rule_condition import RuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of RuleCondition from a JSON string
rule_condition_instance = RuleCondition.from_json(json)
# print the JSON string representation of the object
print(RuleCondition.to_json())

# convert the object into a dict
rule_condition_dict = rule_condition_instance.to_dict()
# create an instance of RuleCondition from a dict
rule_condition_from_dict = RuleCondition.from_dict(rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


