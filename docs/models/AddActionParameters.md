# formkiq_client.model.add_action_parameters.AddActionParameters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ocrParseTypes** | str,  | str,  | OCR: Parse types - TEXT, FORMS, TABLES | [optional] 
**addPdfDetectedCharactersAsText** | bool,  | BoolClass,  | OCR: For the rewriting of the PDF document, converting any image text to searchable text | [optional] 
**url** | str,  | str,  | Webhook: Callback URL | [optional] 
**characterMax** | str,  | str,  | Fulltext: Maximum number of characters (-1 unlimited, Typesense defaults to 2048 characters) | [optional] 
**engine** | str,  | str,  | DocumentTagging: Engine to use for document tagging generation | [optional] must be one of ["chatgpt", ] 
**tags** | str,  | str,  | DocumentTagging: Comma-deliminted list of keywords to generate tags for | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

