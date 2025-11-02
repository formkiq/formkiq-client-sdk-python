# GetEntityTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | [**EntityType**](EntityType.md) |  | [optional] 

## Example

```python
from openapi_client.model.get_entity_type_response import GetEntityTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityTypeResponse from a JSON string
get_entity_type_response_instance = GetEntityTypeResponse.from_json(json)
# print the JSON string representation of the object
print(GetEntityTypeResponse.to_json())

# convert the object into a dict
get_entity_type_response_dict = get_entity_type_response_instance.to_dict()
# create an instance of GetEntityTypeResponse from a dict
get_entity_type_response_from_dict = GetEntityTypeResponse.from_dict(get_entity_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


