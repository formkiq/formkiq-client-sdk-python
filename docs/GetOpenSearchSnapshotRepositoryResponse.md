# GetOpenSearchSnapshotRepositoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s3_repositories** | [**List[OpenSearchS3Repository]**](OpenSearchS3Repository.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_open_search_snapshot_repository_response import GetOpenSearchSnapshotRepositoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenSearchSnapshotRepositoryResponse from a JSON string
get_open_search_snapshot_repository_response_instance = GetOpenSearchSnapshotRepositoryResponse.from_json(json)
# print the JSON string representation of the object
print(GetOpenSearchSnapshotRepositoryResponse.to_json())

# convert the object into a dict
get_open_search_snapshot_repository_response_dict = get_open_search_snapshot_repository_response_instance.to_dict()
# create an instance of GetOpenSearchSnapshotRepositoryResponse from a dict
get_open_search_snapshot_repository_response_from_dict = GetOpenSearchSnapshotRepositoryResponse.from_dict(get_open_search_snapshot_repository_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


