# GetDocumentSyncResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**syncs** | [**List[DocumentSync]**](DocumentSync.md) | List of document syncs | [optional] 

## Example

```python
from formkiq_client.models.get_document_sync_response import GetDocumentSyncResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentSyncResponse from a JSON string
get_document_sync_response_instance = GetDocumentSyncResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentSyncResponse.to_json())

# convert the object into a dict
get_document_sync_response_dict = get_document_sync_response_instance.to_dict()
# create an instance of GetDocumentSyncResponse from a dict
get_document_sync_response_from_dict = GetDocumentSyncResponse.from_dict(get_document_sync_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


