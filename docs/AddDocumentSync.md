# AddDocumentSync


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**AddDocumentSyncService**](AddDocumentSyncService.md) |  | [optional] 
**type** | [**DocumentSyncType**](DocumentSyncType.md) |  | [optional] 

## Example

```python
from formkiq_client.models.add_document_sync import AddDocumentSync

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentSync from a JSON string
add_document_sync_instance = AddDocumentSync.from_json(json)
# print the JSON string representation of the object
print(AddDocumentSync.to_json())

# convert the object into a dict
add_document_sync_dict = add_document_sync_instance.to_dict()
# create an instance of AddDocumentSync from a dict
add_document_sync_from_dict = AddDocumentSync.from_dict(add_document_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


