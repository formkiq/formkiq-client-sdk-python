# formkiq_client.model.set_document_fulltext_request.SetDocumentFulltextRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**contentType** | str,  | str,  | Document Content-Type | [optional] 
**content** | str,  | str,  | Document content | [optional] 
**[contentUrls](#contentUrls)** | list, tuple,  | tuple,  | URL(s) which contain document content | [optional] 
**path** | str,  | str,  | Path or Name of document | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  | List of document tags | [optional] 
**[metadata](#metadata)** | list, tuple,  | tuple,  | List of document Metadata | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# contentUrls

URL(s) which contain document content

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | URL(s) which contain document content | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# tags

List of document tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of document tags | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AddDocumentTag**](AddDocumentTag.md) | [**AddDocumentTag**](AddDocumentTag.md) | [**AddDocumentTag**](AddDocumentTag.md) |  | 

# metadata

List of document Metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of document Metadata | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AddDocumentMetadata**](AddDocumentMetadata.md) | [**AddDocumentMetadata**](AddDocumentMetadata.md) | [**AddDocumentMetadata**](AddDocumentMetadata.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

