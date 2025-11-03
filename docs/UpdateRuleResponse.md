# UpdateRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Rule update message | [optional] 

## Example

```python
from formkiq_client.models.update_rule_response import UpdateRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRuleResponse from a JSON string
update_rule_response_instance = UpdateRuleResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateRuleResponse.to_json())

# convert the object into a dict
update_rule_response_dict = update_rule_response_instance.to_dict()
# create an instance of UpdateRuleResponse from a dict
update_rule_response_from_dict = UpdateRuleResponse.from_dict(update_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


