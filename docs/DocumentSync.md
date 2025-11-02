# DocumentSync


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**DocumentSyncService**](DocumentSyncService.md) |  | [optional] 
**status** | [**DocumentSyncStatus**](DocumentSyncStatus.md) |  | [optional] 
**type** | [**DocumentSyncType**](DocumentSyncType.md) |  | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**sync_date** | **str** | Timestamp of synchronization | [optional] 
**user_id** | **str** | User who added document | [optional] 
**message** | **str** | Document sync message | [optional] 

## Example

```python
from openapi_client.models.document_sync import DocumentSync

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSync from a JSON string
document_sync_instance = DocumentSync.from_json(json)
# print the JSON string representation of the object
print(DocumentSync.to_json())

# convert the object into a dict
document_sync_dict = document_sync_instance.to_dict()
# create an instance of DocumentSync from a dict
document_sync_from_dict = DocumentSync.from_dict(document_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


