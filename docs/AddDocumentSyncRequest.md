# AddDocumentSyncRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync** | [**AddDocumentSync**](AddDocumentSync.md) |  | [optional] 

## Example

```python
from formkiq_client.models.add_document_sync_request import AddDocumentSyncRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentSyncRequest from a JSON string
add_document_sync_request_instance = AddDocumentSyncRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentSyncRequest.to_json())

# convert the object into a dict
add_document_sync_request_dict = add_document_sync_request_instance.to_dict()
# create an instance of AddDocumentSyncRequest from a dict
add_document_sync_request_from_dict = AddDocumentSyncRequest.from_dict(add_document_sync_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


