# SetDocumentVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_key** | **str** | VersionKey returned by the GET /documents/{documentId}/versions to revert to | [optional] 

## Example

```python
from openapi_client.model.set_document_version_request import SetDocumentVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDocumentVersionRequest from a JSON string
set_document_version_request_instance = SetDocumentVersionRequest.from_json(json)
# print the JSON string representation of the object
print(SetDocumentVersionRequest.to_json())

# convert the object into a dict
set_document_version_request_dict = set_document_version_request_instance.to_dict()
# create an instance of SetDocumentVersionRequest from a dict
set_document_version_request_from_dict = SetDocumentVersionRequest.from_dict(set_document_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


