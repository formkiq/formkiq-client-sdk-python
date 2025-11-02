# OpenSearchSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot** | **str** | Snapshot name | [optional] 
**uuid** | **str** | Snapshot’s universally unique identifier (UUID) | [optional] 
**version** | **str** | Open Search version that created the snapshot | [optional] 
**indices** | **List[str]** | Indices in the snapshot | [optional] 
**shards** | [**OpenSearchSnapshotShard**](OpenSearchSnapshotShard.md) |  | [optional] 
**failures** | [**List[OpenSearchSnapshotFailure]**](OpenSearchSnapshotFailure.md) |  | [optional] 
**state** | **str** | Snapshot status. Possible values: IN_PROGRESS, SUCCESS, FAILED, PARTIAL | [optional] 
**start_time** | **str** | Date/time when the snapshot creation process began | [optional] 
**start_time_in_millis** | **float** | Time (in milliseconds) when the snapshot creation process began | [optional] 
**end_time** | **str** | Date/time when the snapshot creation process ended | [optional] 
**end_time_in_millis** | **float** | Time (in milliseconds) when the snapshot creation process ended | [optional] 
**duration_in_millis** | **float** | Total time (in milliseconds) that the snapshot creation process lasted | [optional] 

## Example

```python
from openapi_client.models.open_search_snapshot import OpenSearchSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of OpenSearchSnapshot from a JSON string
open_search_snapshot_instance = OpenSearchSnapshot.from_json(json)
# print the JSON string representation of the object
print(OpenSearchSnapshot.to_json())

# convert the object into a dict
open_search_snapshot_dict = open_search_snapshot_instance.to_dict()
# create an instance of OpenSearchSnapshot from a dict
open_search_snapshot_from_dict = OpenSearchSnapshot.from_dict(open_search_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


