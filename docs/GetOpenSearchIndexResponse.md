# GetOpenSearchIndexResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_settings** | [**OpenSearchIndex**](OpenSearchIndex.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_open_search_index_response import GetOpenSearchIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenSearchIndexResponse from a JSON string
get_open_search_index_response_instance = GetOpenSearchIndexResponse.from_json(json)
# print the JSON string representation of the object
print(GetOpenSearchIndexResponse.to_json())

# convert the object into a dict
get_open_search_index_response_dict = get_open_search_index_response_instance.to_dict()
# create an instance of GetOpenSearchIndexResponse from a dict
get_open_search_index_response_from_dict = GetOpenSearchIndexResponse.from_dict(get_open_search_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


