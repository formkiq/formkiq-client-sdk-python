# AddRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | Rule Identifier | [optional] 

## Example

```python
from formkiq_client.models.add_rule_response import AddRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddRuleResponse from a JSON string
add_rule_response_instance = AddRuleResponse.from_json(json)
# print the JSON string representation of the object
print(AddRuleResponse.to_json())

# convert the object into a dict
add_rule_response_dict = add_rule_response_instance.to_dict()
# create an instance of AddRuleResponse from a dict
add_rule_response_form_dict = add_rule_response.from_dict(add_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


