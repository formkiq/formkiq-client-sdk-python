# formkiq_client.model.search_result_document.SearchResultDocument

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**siteId** | str,  | str,  | Site Identifier | [optional] 
**path** | str,  | str,  | Path or Name of document | [optional] 
**insertedDate** | str,  | str,  | Inserted Timestamp | [optional] 
**lastModifiedDate** | str,  | str,  | Last Modified Timestamp | [optional] 
**folder** | bool,  | BoolClass,  | Is Result a Document Folder | [optional] 
**indexKey** | str,  | str,  | populated if search result are from an index | [optional] 
**checksum** | str,  | str,  | Document checksum, changes when document file changes | [optional] 
**documentId** | str,  | str,  | Document Identifier | [optional] 
**contentType** | str,  | str,  | Document Content-Type | [optional] 
**userId** | str,  | str,  | User who added document | [optional] 
**contentLength** | decimal.Decimal, int,  | decimal.Decimal,  | Document size | [optional] 
**versionId** | str,  | str,  | Document version | [optional] 
**belongsToDocumentId** | str,  | str,  | Parent Document Identifier | [optional] 
**matchedTag** | [**DocumentSearchMatchTag**](DocumentSearchMatchTag.md) | [**DocumentSearchMatchTag**](DocumentSearchMatchTag.md) |  | [optional] 
**[tags](#tags)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

