# formkiq_client.model.only_office_config.OnlyOfficeConfig

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**onlyOfficeUrl** | str,  | str,  | URL of the ONLYOFFICE application | [optional] 
**token** | str,  | str,  | ONLYOFFICE security token | [optional] 
**documentType** | str,  | str,  | Type of document (https://api.onlyoffice.com/editors/config/) | [optional] 
**editorConfig** | [**OnlyOfficeEditorConfig**](OnlyOfficeEditorConfig.md) | [**OnlyOfficeEditorConfig**](OnlyOfficeEditorConfig.md) |  | [optional] 
**document** | [**OnlyOfficeConfigDocument**](OnlyOfficeConfigDocument.md) | [**OnlyOfficeConfigDocument**](OnlyOfficeConfigDocument.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

