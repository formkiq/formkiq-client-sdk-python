# OpenSearchIndexSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_replicas** | **str** | The number of replicas per shard | [optional] 
**number_of_shards** | **str** | The number of shards in index | [optional] 

## Example

```python
from openapi_client.model.open_search_index_setting import OpenSearchIndexSetting

# TODO update the JSON string below
json = "{}"
# create an instance of OpenSearchIndexSetting from a JSON string
open_search_index_setting_instance = OpenSearchIndexSetting.from_json(json)
# print the JSON string representation of the object
print(OpenSearchIndexSetting.to_json())

# convert the object into a dict
open_search_index_setting_dict = open_search_index_setting_instance.to_dict()
# create an instance of OpenSearchIndexSetting from a dict
open_search_index_setting_from_dict = OpenSearchIndexSetting.from_dict(open_search_index_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


