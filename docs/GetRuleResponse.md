# GetRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | [**Rule**](Rule.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_rule_response import GetRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRuleResponse from a JSON string
get_rule_response_instance = GetRuleResponse.from_json(json)
# print the JSON string representation of the object
print(GetRuleResponse.to_json())

# convert the object into a dict
get_rule_response_dict = get_rule_response_instance.to_dict()
# create an instance of GetRuleResponse from a dict
get_rule_response_from_dict = GetRuleResponse.from_dict(get_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


