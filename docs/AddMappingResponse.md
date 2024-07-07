# AddMappingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping_id** | **str** | Mapping Identifier | [optional] 

## Example

```python
from formkiq_client.models.add_mapping_response import AddMappingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddMappingResponse from a JSON string
add_mapping_response_instance = AddMappingResponse.from_json(json)
# print the JSON string representation of the object
print(AddMappingResponse.to_json())

# convert the object into a dict
add_mapping_response_dict = add_mapping_response_instance.to_dict()
# create an instance of AddMappingResponse from a dict
add_mapping_response_from_dict = AddMappingResponse.from_dict(add_mapping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


