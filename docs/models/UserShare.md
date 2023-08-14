# formkiq_client.model.user_share.UserShare

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**group** | str,  | str,  | Name of Share Group | [optional] 
**shareKey** | str,  | str,  | Share Identifier | [optional] 
**type** | str,  | str,  | Type of Document | [optional] must be one of ["FOLDER", ] 
**[permissions](#permissions)** | list, tuple,  | tuple,  | List of share permissions | [optional] 
**siteId** | str,  | str,  | Site Identifier | [optional] 
**path** | str,  | str,  | Path or Name of document | [optional] 
**userId** | str,  | str,  | User who created share | [optional] 
**permissionType** | str,  | str,  | Type of share | [optional] must be one of ["GROUP", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# permissions

List of share permissions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of share permissions | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["READ", "WRITE", "DELETE", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

