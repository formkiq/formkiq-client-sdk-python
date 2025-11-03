# GetRulesetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ruleset** | [**Ruleset**](Ruleset.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_ruleset_response import GetRulesetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRulesetResponse from a JSON string
get_ruleset_response_instance = GetRulesetResponse.from_json(json)
# print the JSON string representation of the object
print(GetRulesetResponse.to_json())

# convert the object into a dict
get_ruleset_response_dict = get_ruleset_response_instance.to_dict()
# create an instance of GetRulesetResponse from a dict
get_ruleset_response_from_dict = GetRulesetResponse.from_dict(get_ruleset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


