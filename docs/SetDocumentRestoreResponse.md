# SetDocumentRestoreResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Document Document restore message | [optional] 

## Example

```python
from formkiq_client.models.set_document_restore_response import SetDocumentRestoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetDocumentRestoreResponse from a JSON string
set_document_restore_response_instance = SetDocumentRestoreResponse.from_json(json)
# print the JSON string representation of the object
print(SetDocumentRestoreResponse.to_json())

# convert the object into a dict
set_document_restore_response_dict = set_document_restore_response_instance.to_dict()
# create an instance of SetDocumentRestoreResponse from a dict
set_document_restore_response_from_dict = SetDocumentRestoreResponse.from_dict(set_document_restore_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


