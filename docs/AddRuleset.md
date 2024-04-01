# AddRuleset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Ruleset description | [optional] 
**priority** | **float** | Ruleset priority | [optional] 
**version** | **float** | Ruleset version | [optional] 
**status** | [**RulesetStatus**](RulesetStatus.md) |  | [optional] 

## Example

```python
from formkiq_client.models.add_ruleset import AddRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of AddRuleset from a JSON string
add_ruleset_instance = AddRuleset.from_json(json)
# print the JSON string representation of the object
print(AddRuleset.to_json())

# convert the object into a dict
add_ruleset_dict = add_ruleset_instance.to_dict()
# create an instance of AddRuleset from a dict
add_ruleset_form_dict = add_ruleset.from_dict(add_ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


