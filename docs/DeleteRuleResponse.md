# DeleteRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Result message | [optional] 

## Example

```python
from formkiq_client.models.delete_rule_response import DeleteRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRuleResponse from a JSON string
delete_rule_response_instance = DeleteRuleResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteRuleResponse.to_json())

# convert the object into a dict
delete_rule_response_dict = delete_rule_response_instance.to_dict()
# create an instance of DeleteRuleResponse from a dict
delete_rule_response_form_dict = delete_rule_response.from_dict(delete_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


