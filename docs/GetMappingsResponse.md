# GetMappingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mappings** | [**List[Mapping]**](Mapping.md) |  | [optional] 
**next** | **str** | Next page of results token | [optional] 

## Example

```python
from openapi_client.model.get_mappings_response import GetMappingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMappingsResponse from a JSON string
get_mappings_response_instance = GetMappingsResponse.from_json(json)
# print the JSON string representation of the object
print(GetMappingsResponse.to_json())

# convert the object into a dict
get_mappings_response_dict = get_mappings_response_instance.to_dict()
# create an instance of GetMappingsResponse from a dict
get_mappings_response_from_dict = GetMappingsResponse.from_dict(get_mappings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


