# GetDocumentOcrResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_urls** | **List[str]** | Presigned S3 Urls for the OCR content | [optional] 
**data** | **str** | OCR text result | [optional] 
**ocr_engine** | **str** | The OCR technique used | [optional] 
**ocr_status** | **str** | The status of the OCR request | [optional] 
**content_type** | **str** | Document Content-Type | [optional] 
**is_base64** | **bool** | Is the content Base64-encoded? | [optional] 
**user_id** | **str** | User who requested the OCR | [optional] 
**document_id** | **str** | Document Identifier | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 

## Example

```python
from formkiq_client.models.get_document_ocr_response import GetDocumentOcrResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentOcrResponse from a JSON string
get_document_ocr_response_instance = GetDocumentOcrResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentOcrResponse.to_json())

# convert the object into a dict
get_document_ocr_response_dict = get_document_ocr_response_instance.to_dict()
# create an instance of GetDocumentOcrResponse from a dict
get_document_ocr_response_form_dict = get_document_ocr_response.from_dict(get_document_ocr_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


