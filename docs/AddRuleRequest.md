# AddRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | [**AddRule**](AddRule.md) |  | [optional] 

## Example

```python
from openapi_client.model.add_rule_request import AddRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddRuleRequest from a JSON string
add_rule_request_instance = AddRuleRequest.from_json(json)
# print the JSON string representation of the object
print(AddRuleRequest.to_json())

# convert the object into a dict
add_rule_request_dict = add_rule_request_instance.to_dict()
# create an instance of AddRuleRequest from a dict
add_rule_request_from_dict = AddRuleRequest.from_dict(add_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


