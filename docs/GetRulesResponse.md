# GetRulesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**rules** | [**List[Rule]**](Rule.md) | List of rules | [optional] 

## Example

```python
from formkiq_client.models.get_rules_response import GetRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRulesResponse from a JSON string
get_rules_response_instance = GetRulesResponse.from_json(json)
# print the JSON string representation of the object
print(GetRulesResponse.to_json())

# convert the object into a dict
get_rules_response_dict = get_rules_response_instance.to_dict()
# create an instance of GetRulesResponse from a dict
get_rules_response_from_dict = GetRulesResponse.from_dict(get_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


