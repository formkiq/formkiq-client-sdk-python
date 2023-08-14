# formkiq_client.model.add_tag_schema_tags.AddTagSchemaTags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[compositeKeys](#compositeKeys)** | list, tuple,  | tuple,  | List of Composite Keys | [optional] 
**[required](#required)** | list, tuple,  | tuple,  | List of Required Tags | [optional] 
**[optional](#optional)** | list, tuple,  | tuple,  | List of Optional Tags | [optional] 
**allowAdditionalTags** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of True
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# compositeKeys

List of Composite Keys

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Composite Keys | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TagSchemaCompositeKey**](TagSchemaCompositeKey.md) | [**TagSchemaCompositeKey**](TagSchemaCompositeKey.md) | [**TagSchemaCompositeKey**](TagSchemaCompositeKey.md) |  | 

# required

List of Required Tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Required Tags | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TagSchemaRequired**](TagSchemaRequired.md) | [**TagSchemaRequired**](TagSchemaRequired.md) | [**TagSchemaRequired**](TagSchemaRequired.md) |  | 

# optional

List of Optional Tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Optional Tags | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TagSchemaOptional**](TagSchemaOptional.md) | [**TagSchemaOptional**](TagSchemaOptional.md) | [**TagSchemaOptional**](TagSchemaOptional.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

