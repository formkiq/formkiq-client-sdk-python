# formkiq_client.model.esignature_docusign_request.EsignatureDocusignRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**emailSubject** | str,  | str,  | Email Subject | [optional] 
**status** | str,  | str,  | The status of the request | [optional] must be one of ["created", "sent", ] 
**developmentMode** | bool,  | BoolClass,  | Whether to enable developer mode | [optional] 
**[signers](#signers)** | list, tuple,  | tuple,  | List of DocuSign Signers | [optional] 
**[carbonCopies](#carbonCopies)** | list, tuple,  | tuple,  | List of DocuSign Carbon Copies | [optional] 
**[recipientTabs](#recipientTabs)** | list, tuple,  | tuple,  | List of DocuSign Recipient Tabs | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# signers

List of DocuSign Signers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of DocuSign Signers | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EsignatureDocusignSigner**](EsignatureDocusignSigner.md) | [**EsignatureDocusignSigner**](EsignatureDocusignSigner.md) | [**EsignatureDocusignSigner**](EsignatureDocusignSigner.md) |  | 

# carbonCopies

List of DocuSign Carbon Copies

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of DocuSign Carbon Copies | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EsignatureDocusignCarbonCopy**](EsignatureDocusignCarbonCopy.md) | [**EsignatureDocusignCarbonCopy**](EsignatureDocusignCarbonCopy.md) | [**EsignatureDocusignCarbonCopy**](EsignatureDocusignCarbonCopy.md) |  | 

# recipientTabs

List of DocuSign Recipient Tabs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of DocuSign Recipient Tabs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EsignatureDocusignRecipientTab**](EsignatureDocusignRecipientTab.md) | [**EsignatureDocusignRecipientTab**](EsignatureDocusignRecipientTab.md) | [**EsignatureDocusignRecipientTab**](EsignatureDocusignRecipientTab.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

