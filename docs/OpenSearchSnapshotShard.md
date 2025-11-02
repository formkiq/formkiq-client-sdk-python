# OpenSearchSnapshotShard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | Total number of shards | [optional] 
**failed** | **float** | Failed number of shards | [optional] 
**successful** | **float** | Successful number of shards | [optional] 

## Example

```python
from openapi_client.model.open_search_snapshot_shard import OpenSearchSnapshotShard

# TODO update the JSON string below
json = "{}"
# create an instance of OpenSearchSnapshotShard from a JSON string
open_search_snapshot_shard_instance = OpenSearchSnapshotShard.from_json(json)
# print the JSON string representation of the object
print(OpenSearchSnapshotShard.to_json())

# convert the object into a dict
open_search_snapshot_shard_dict = open_search_snapshot_shard_instance.to_dict()
# create an instance of OpenSearchSnapshotShard from a dict
open_search_snapshot_shard_from_dict = OpenSearchSnapshotShard.from_dict(open_search_snapshot_shard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


