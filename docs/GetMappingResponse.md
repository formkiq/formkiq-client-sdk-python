# GetMappingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**Mapping**](Mapping.md) |  | [optional] 

## Example

```python
from openapi_client.model.get_mapping_response import GetMappingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMappingResponse from a JSON string
get_mapping_response_instance = GetMappingResponse.from_json(json)
# print the JSON string representation of the object
print(GetMappingResponse.to_json())

# convert the object into a dict
get_mapping_response_dict = get_mapping_response_instance.to_dict()
# create an instance of GetMappingResponse from a dict
get_mapping_response_from_dict = GetMappingResponse.from_dict(get_mapping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


