# GetEntityTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**entity_types** | [**List[EntityType]**](EntityType.md) | List of Entity Types | [optional] 

## Example

```python
from openapi_client.models.get_entity_types_response import GetEntityTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityTypesResponse from a JSON string
get_entity_types_response_instance = GetEntityTypesResponse.from_json(json)
# print the JSON string representation of the object
print(GetEntityTypesResponse.to_json())

# convert the object into a dict
get_entity_types_response_dict = get_entity_types_response_instance.to_dict()
# create an instance of GetEntityTypesResponse from a dict
get_entity_types_response_from_dict = GetEntityTypesResponse.from_dict(get_entity_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


