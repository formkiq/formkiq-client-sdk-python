# formkiq_client.model.document_search.DocumentSearch

Document tag search criteria

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Document tag search criteria | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  | Full text search | [optional] 
**meta** | [**DocumentSearchItemMeta**](DocumentSearchItemMeta.md) | [**DocumentSearchItemMeta**](DocumentSearchItemMeta.md) |  | [optional] 
**tag** | [**DocumentSearchItemTag**](DocumentSearchItemTag.md) | [**DocumentSearchItemTag**](DocumentSearchItemTag.md) |  | [optional] 
**[documentIds](#documentIds)** | list, tuple,  | tuple,  | List of DocumentIds to filter search results on | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# documentIds

List of DocumentIds to filter search results on

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of DocumentIds to filter search results on | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

