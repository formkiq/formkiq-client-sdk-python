# UpdateRulesetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ruleset** | [**UpdateRuleset**](UpdateRuleset.md) |  | 

## Example

```python
from openapi_client.model.update_ruleset_request import UpdateRulesetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRulesetRequest from a JSON string
update_ruleset_request_instance = UpdateRulesetRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRulesetRequest.to_json())

# convert the object into a dict
update_ruleset_request_dict = update_ruleset_request_instance.to_dict()
# create an instance of UpdateRulesetRequest from a dict
update_ruleset_request_from_dict = UpdateRulesetRequest.from_dict(update_ruleset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


