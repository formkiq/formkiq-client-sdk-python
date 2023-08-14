# formkiq_client.model.get_document_response.GetDocumentResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**documentId** | str,  | str,  | Document Identifier | 
**siteId** | str,  | str,  | Site Identifier | [optional] 
**path** | str,  | str,  | Path or Name of document | [optional] 
**insertedDate** | str,  | str,  | Inserted Timestamp | [optional] 
**lastModifiedDate** | str,  | str,  | Last Modified Timestamp | [optional] 
**checksum** | str,  | str,  | Document checksum, changes when document file changes | [optional] 
**contentType** | str,  | str,  | Document Content-Type | [optional] 
**userId** | str,  | str,  | User who added document | [optional] 
**contentLength** | decimal.Decimal, int,  | decimal.Decimal,  | Document size | [optional] 
**versionId** | str,  | str,  | Document version | [optional] 
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
[**ChildDocument**](ChildDocument.md) | [**ChildDocument**](ChildDocument.md) | [**ChildDocument**](ChildDocument.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

