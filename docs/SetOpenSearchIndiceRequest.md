# SetOpenSearchIndiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_name** | **str** | The name of the index to set for SiteId | [optional] 

## Example

```python
from openapi_client.models.set_open_search_indice_request import SetOpenSearchIndiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetOpenSearchIndiceRequest from a JSON string
set_open_search_indice_request_instance = SetOpenSearchIndiceRequest.from_json(json)
# print the JSON string representation of the object
print(SetOpenSearchIndiceRequest.to_json())

# convert the object into a dict
set_open_search_indice_request_dict = set_open_search_indice_request_instance.to_dict()
# create an instance of SetOpenSearchIndiceRequest from a dict
set_open_search_indice_request_from_dict = SetOpenSearchIndiceRequest.from_dict(set_open_search_indice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


