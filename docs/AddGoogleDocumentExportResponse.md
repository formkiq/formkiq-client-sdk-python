# AddGoogleDocumentExportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Exported document identifier | [optional] 

## Example

```python
from formkiq_client.models.add_google_document_export_response import AddGoogleDocumentExportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddGoogleDocumentExportResponse from a JSON string
add_google_document_export_response_instance = AddGoogleDocumentExportResponse.from_json(json)
# print the JSON string representation of the object
print(AddGoogleDocumentExportResponse.to_json())

# convert the object into a dict
add_google_document_export_response_dict = add_google_document_export_response_instance.to_dict()
# create an instance of AddGoogleDocumentExportResponse from a dict
add_google_document_export_response_from_dict = AddGoogleDocumentExportResponse.from_dict(add_google_document_export_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


