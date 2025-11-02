# OpenSearchSnapshotFailure

Details about a failure for a specific shard in a snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** | The index name. | [optional] 
**index_uuid** | **str** | UUID of the index. | [optional] 
**shard_id** | **int** | Shard identifier. | [optional] 
**reason** | **str** | Full exception/message explaining why the failure occurred. | [optional] 
**node_id** | **str** | ID of the node handling that shard. | [optional] 
**status** | **str** | Status of the failure (e.g., INTERNAL_SERVER_ERROR). | [optional] 

## Example

```python
from openapi_client.models.open_search_snapshot_failure import OpenSearchSnapshotFailure

# TODO update the JSON string below
json = "{}"
# create an instance of OpenSearchSnapshotFailure from a JSON string
open_search_snapshot_failure_instance = OpenSearchSnapshotFailure.from_json(json)
# print the JSON string representation of the object
print(OpenSearchSnapshotFailure.to_json())

# convert the object into a dict
open_search_snapshot_failure_dict = open_search_snapshot_failure_instance.to_dict()
# create an instance of OpenSearchSnapshotFailure from a dict
open_search_snapshot_failure_from_dict = OpenSearchSnapshotFailure.from_dict(open_search_snapshot_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


