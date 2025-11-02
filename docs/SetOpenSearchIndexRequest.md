# SetOpenSearchIndexRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_settings** | [**OpenSearchIndexSetting**](OpenSearchIndexSetting.md) |  | [optional] 

## Example

```python
from formkiq_client.models.set_open_search_index_request import SetOpenSearchIndexRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetOpenSearchIndexRequest from a JSON string
set_open_search_index_request_instance = SetOpenSearchIndexRequest.from_json(json)
# print the JSON string representation of the object
print(SetOpenSearchIndexRequest.to_json())

# convert the object into a dict
set_open_search_index_request_dict = set_open_search_index_request_instance.to_dict()
# create an instance of SetOpenSearchIndexRequest from a dict
set_open_search_index_request_from_dict = SetOpenSearchIndexRequest.from_dict(set_open_search_index_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


