# formkiq_client.model.get_document_sync.GetDocumentSync

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**service** | str,  | str,  | To which service the data was synced | [optional] must be one of ["TYPESENSE", "OPENSEARCH", ] 
**status** | str,  | str,  | The status of the sync | [optional] must be one of ["COMPLETE", "FAILED", ] 
**type** | str,  | str,  | The type of the sync | [optional] must be one of ["METADATA", "TAG", ] 
**syncDate** | str,  | str,  | Timestamp of synchronization | [optional] 
**userId** | str,  | str,  | User who added document | [optional] 
**message** | str,  | str,  | Document sync message | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

