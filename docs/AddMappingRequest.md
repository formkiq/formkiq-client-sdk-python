# AddMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**AddMapping**](AddMapping.md) |  | [optional] 

## Example

```python
from formkiq_client.models.add_mapping_request import AddMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddMappingRequest from a JSON string
add_mapping_request_instance = AddMappingRequest.from_json(json)
# print the JSON string representation of the object
print(AddMappingRequest.to_json())

# convert the object into a dict
add_mapping_request_dict = add_mapping_request_instance.to_dict()
# create an instance of AddMappingRequest from a dict
add_mapping_request_from_dict = AddMappingRequest.from_dict(add_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


