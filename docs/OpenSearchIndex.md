# OpenSearchIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_replicas** | **str** | The number of replicas per shard | [optional] 
**number_of_shards** | **str** | The number of shards in index | [optional] 
**document_count** | **str** | The number of documents in index | [optional] 
**store_size** | **str** | The store size of the index | [optional] 
**name** | **str** | Name of Index | [optional] 
**aliases** | [**List[OpenSearchAlias]**](OpenSearchAlias.md) |  | [optional] 

## Example

```python
from openapi_client.model.open_search_index import OpenSearchIndex

# TODO update the JSON string below
json = "{}"
# create an instance of OpenSearchIndex from a JSON string
open_search_index_instance = OpenSearchIndex.from_json(json)
# print the JSON string representation of the object
print(OpenSearchIndex.to_json())

# convert the object into a dict
open_search_index_dict = open_search_index_instance.to_dict()
# create an instance of OpenSearchIndex from a dict
open_search_index_from_dict = OpenSearchIndex.from_dict(open_search_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


