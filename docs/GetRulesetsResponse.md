# GetRulesetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**rulesets** | [**List[Ruleset]**](Ruleset.md) | List of rulesets | [optional] 

## Example

```python
from formkiq_client.models.get_rulesets_response import GetRulesetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRulesetsResponse from a JSON string
get_rulesets_response_instance = GetRulesetsResponse.from_json(json)
# print the JSON string representation of the object
print(GetRulesetsResponse.to_json())

# convert the object into a dict
get_rulesets_response_dict = get_rulesets_response_instance.to_dict()
# create an instance of GetRulesetsResponse from a dict
get_rulesets_response_form_dict = get_rulesets_response.from_dict(get_rulesets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


