# formkiq_client.model.add_document_response.AddDocumentResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**documentId** | str,  | str,  | Document Identifier | [optional] 
**siteId** | str,  | str,  | Site Identifier | [optional] 
**uploadUrl** | str,  | str,  | Url to upload document to | [optional] 
**[documents](#documents)** | list, tuple,  | tuple,  | List of child documents | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# documents

List of child documents

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of child documents | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AddChildDocumentResponse**](AddChildDocumentResponse.md) | [**AddChildDocumentResponse**](AddChildDocumentResponse.md) | [**AddChildDocumentResponse**](AddChildDocumentResponse.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

