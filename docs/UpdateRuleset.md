# UpdateRuleset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Ruleset description | [optional] 
**priority** | **float** | Ruleset priority | [optional] 
**version** | **float** | Ruleset version | [optional] 
**status** | [**RulesetStatus**](RulesetStatus.md) |  | [optional] 

## Example

```python
from formkiq_client.models.update_ruleset import UpdateRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRuleset from a JSON string
update_ruleset_instance = UpdateRuleset.from_json(json)
# print the JSON string representation of the object
print(UpdateRuleset.to_json())

# convert the object into a dict
update_ruleset_dict = update_ruleset_instance.to_dict()
# create an instance of UpdateRuleset from a dict
update_ruleset_form_dict = update_ruleset.from_dict(update_ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


