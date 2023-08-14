# formkiq_client.model.document_search_item_meta.DocumentSearchItemMeta

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**folder** | str,  | str,  | Searches for a folder | [optional] 
**path** | str,  | str,  | Searches for a Path of document | [optional] 
**indexType** | str,  | str,  | Searches in an index | [optional] must be one of ["folder", ] 
**indexFilterBeginsWith** | str,  | str,  | Returns index records that begins with a particular substring | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

