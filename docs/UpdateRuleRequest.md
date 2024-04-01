# UpdateRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | [**UpdateRule**](UpdateRule.md) |  | [optional] 

## Example

```python
from formkiq_client.models.update_rule_request import UpdateRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRuleRequest from a JSON string
update_rule_request_instance = UpdateRuleRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRuleRequest.to_json())

# convert the object into a dict
update_rule_request_dict = update_rule_request_instance.to_dict()
# create an instance of UpdateRuleRequest from a dict
update_rule_request_form_dict = update_rule_request.from_dict(update_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


