# AddRulesetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ruleset** | [**AddRuleset**](AddRuleset.md) |  | 

## Example

```python
from formkiq_client.models.add_ruleset_request import AddRulesetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddRulesetRequest from a JSON string
add_ruleset_request_instance = AddRulesetRequest.from_json(json)
# print the JSON string representation of the object
print(AddRulesetRequest.to_json())

# convert the object into a dict
add_ruleset_request_dict = add_ruleset_request_instance.to_dict()
# create an instance of AddRulesetRequest from a dict
add_ruleset_request_from_dict = AddRulesetRequest.from_dict(add_ruleset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


