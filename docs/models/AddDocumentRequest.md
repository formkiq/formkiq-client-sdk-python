# formkiq_client.model.add_document_request.AddDocumentRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**content** | str,  | str,  | Document content | 
**tagSchemaId** | str,  | str,  | Tag Schema Id | [optional] 
**path** | str,  | str,  | Path or Name of document | [optional] 
**contentType** | str,  | str,  | Document media type | [optional] 
**isBase64** | bool,  | BoolClass,  | Is the content Base64-encoded? | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  | List of document tags | [optional] 
**[metadata](#metadata)** | list, tuple,  | tuple,  | List of document Metadata | [optional] 
**[actions](#actions)** | list, tuple,  | tuple,  | List of Actions | [optional] 
**[documents](#documents)** | list, tuple,  | tuple,  | List of child documents | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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

# actions

List of Actions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Actions | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AddAction**](AddAction.md) | [**AddAction**](AddAction.md) | [**AddAction**](AddAction.md) |  | 

# documents

List of child documents

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of child documents | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AddChildDocument**](AddChildDocument.md) | [**AddChildDocument**](AddChildDocument.md) | [**AddChildDocument**](AddChildDocument.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

