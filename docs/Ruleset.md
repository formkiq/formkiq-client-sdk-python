# Ruleset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ruleset_id** | **str** | Ruleset identifier | [optional] 
**description** | **str** | Ruleset description | [optional] 
**priority** | **float** | Ruleset priority | [optional] 
**version** | **float** | Ruleset version | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**status** | [**RulesetStatus**](RulesetStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.ruleset import Ruleset

# TODO update the JSON string below
json = "{}"
# create an instance of Ruleset from a JSON string
ruleset_instance = Ruleset.from_json(json)
# print the JSON string representation of the object
print(Ruleset.to_json())

# convert the object into a dict
ruleset_dict = ruleset_instance.to_dict()
# create an instance of Ruleset from a dict
ruleset_from_dict = Ruleset.from_dict(ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


