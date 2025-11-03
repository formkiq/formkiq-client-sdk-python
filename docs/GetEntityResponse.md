# GetEntityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**Entity**](Entity.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_entity_response import GetEntityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityResponse from a JSON string
get_entity_response_instance = GetEntityResponse.from_json(json)
# print the JSON string representation of the object
print(GetEntityResponse.to_json())

# convert the object into a dict
get_entity_response_dict = get_entity_response_instance.to_dict()
# create an instance of GetEntityResponse from a dict
get_entity_response_from_dict = GetEntityResponse.from_dict(get_entity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


