# AddGoogleDocumentExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path of exported file | [optional] 
**output_type** | [**GoogleExportOutputType**](GoogleExportOutputType.md) |  | [optional] 

## Example

```python
from openapi_client.model.add_google_document_export_request import AddGoogleDocumentExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddGoogleDocumentExportRequest from a JSON string
add_google_document_export_request_instance = AddGoogleDocumentExportRequest.from_json(json)
# print the JSON string representation of the object
print(AddGoogleDocumentExportRequest.to_json())

# convert the object into a dict
add_google_document_export_request_dict = add_google_document_export_request_instance.to_dict()
# create an instance of AddGoogleDocumentExportRequest from a dict
add_google_document_export_request_from_dict = AddGoogleDocumentExportRequest.from_dict(add_google_document_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


