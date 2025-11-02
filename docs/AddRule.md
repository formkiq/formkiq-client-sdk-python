# AddRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **float** | Rule priority | [optional] 
**description** | **str** | Rule description | [optional] 
**workflow_id** | **str** | Workflow to start on matching of conditions | [optional] 
**status** | [**RulesetStatus**](RulesetStatus.md) |  | [optional] 
**conditions** | [**RuleCondition**](RuleCondition.md) |  | [optional] 

## Example

```python
from openapi_client.model.add_rule import AddRule

# TODO update the JSON string below
json = "{}"
# create an instance of AddRule from a JSON string
add_rule_instance = AddRule.from_json(json)
# print the JSON string representation of the object
print(AddRule.to_json())

# convert the object into a dict
add_rule_dict = add_rule_instance.to_dict()
# create an instance of AddRule from a dict
add_rule_from_dict = AddRule.from_dict(add_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


