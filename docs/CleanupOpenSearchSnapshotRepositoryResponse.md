# CleanupOpenSearchSnapshotRepositoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The OpenSearch cleanup snapshot repository response. | [optional] 

## Example

```python
from formkiq_client.models.cleanup_open_search_snapshot_repository_response import CleanupOpenSearchSnapshotRepositoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CleanupOpenSearchSnapshotRepositoryResponse from a JSON string
cleanup_open_search_snapshot_repository_response_instance = CleanupOpenSearchSnapshotRepositoryResponse.from_json(json)
# print the JSON string representation of the object
print(CleanupOpenSearchSnapshotRepositoryResponse.to_json())

# convert the object into a dict
cleanup_open_search_snapshot_repository_response_dict = cleanup_open_search_snapshot_repository_response_instance.to_dict()
# create an instance of CleanupOpenSearchSnapshotRepositoryResponse from a dict
cleanup_open_search_snapshot_repository_response_from_dict = CleanupOpenSearchSnapshotRepositoryResponse.from_dict(cleanup_open_search_snapshot_repository_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


