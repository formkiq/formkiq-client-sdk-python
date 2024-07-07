# UpdateRulesetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Ruleset update message | [optional] 

## Example

```python
from formkiq_client.models.update_ruleset_response import UpdateRulesetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRulesetResponse from a JSON string
update_ruleset_response_instance = UpdateRulesetResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateRulesetResponse.to_json())

# convert the object into a dict
update_ruleset_response_dict = update_ruleset_response_instance.to_dict()
# create an instance of UpdateRulesetResponse from a dict
update_ruleset_response_from_dict = UpdateRulesetResponse.from_dict(update_ruleset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


