# GetDocumentSync


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**DocumentSyncService**](DocumentSyncService.md) |  | [optional] 
**status** | [**DocumentSyncStatus**](DocumentSyncStatus.md) |  | [optional] 
**type** | [**DocumentSyncType**](DocumentSyncType.md) |  | [optional] 
**sync_date** | **str** | Timestamp of synchronization | [optional] 
**user_id** | **str** | User who added document | [optional] 
**message** | **str** | Document sync message | [optional] 

## Example

```python
from formkiq_client.models.get_document_sync import GetDocumentSync

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentSync from a JSON string
get_document_sync_instance = GetDocumentSync.from_json(json)
# print the JSON string representation of the object
print(GetDocumentSync.to_json())

# convert the object into a dict
get_document_sync_dict = get_document_sync_instance.to_dict()
# create an instance of GetDocumentSync from a dict
get_document_sync_from_dict = GetDocumentSync.from_dict(get_document_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


