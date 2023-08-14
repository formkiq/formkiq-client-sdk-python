# formkiq_client.model.get_document_ocr_response.GetDocumentOcrResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**data** | str,  | str,  | OCR text result | [optional] 
**ocrEngine** | str,  | str,  | The OCR technique used | [optional] 
**ocrStatus** | str,  | str,  | The status of the OCR request | [optional] 
**contentType** | str,  | str,  | Document Content-Type | [optional] 
**isBase64** | bool,  | BoolClass,  | Is the content Base64-encoded? | [optional] 
**userId** | str,  | str,  | User who requested the OCR | [optional] 
**documentId** | str,  | str,  | Document Identifier | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

