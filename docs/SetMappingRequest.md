# SetMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**AddMapping**](AddMapping.md) |  | [optional] 

## Example

```python
from formkiq_client.models.set_mapping_request import SetMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetMappingRequest from a JSON string
set_mapping_request_instance = SetMappingRequest.from_json(json)
# print the JSON string representation of the object
print(SetMappingRequest.to_json())

# convert the object into a dict
set_mapping_request_dict = set_mapping_request_instance.to_dict()
# create an instance of SetMappingRequest from a dict
set_mapping_request_from_dict = SetMappingRequest.from_dict(set_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


