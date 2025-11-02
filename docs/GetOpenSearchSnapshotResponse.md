# GetOpenSearchSnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshots** | [**List[OpenSearchSnapshot]**](OpenSearchSnapshot.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_open_search_snapshot_response import GetOpenSearchSnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenSearchSnapshotResponse from a JSON string
get_open_search_snapshot_response_instance = GetOpenSearchSnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(GetOpenSearchSnapshotResponse.to_json())

# convert the object into a dict
get_open_search_snapshot_response_dict = get_open_search_snapshot_response_instance.to_dict()
# create an instance of GetOpenSearchSnapshotResponse from a dict
get_open_search_snapshot_response_from_dict = GetOpenSearchSnapshotResponse.from_dict(get_open_search_snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


