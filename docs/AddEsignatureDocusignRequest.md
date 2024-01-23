# AddEsignatureDocusignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_subject** | **str** | Email Subject | [optional] 
**status** | **str** | The status of the request | [optional] 
**development_mode** | **bool** | Whether to enable developer mode | [optional] 
**signers** | [**List[EsignatureDocusignSigner]**](EsignatureDocusignSigner.md) | List of DocuSign Signers | [optional] 
**carbon_copies** | [**List[EsignatureDocusignCarbonCopy]**](EsignatureDocusignCarbonCopy.md) | List of DocuSign Carbon Copies | [optional] 
**recipient_tabs** | [**List[EsignatureDocusignRecipientTab]**](EsignatureDocusignRecipientTab.md) | List of DocuSign Recipient Tabs | [optional] 

## Example

```python
from formkiq_client.models.add_esignature_docusign_request import AddEsignatureDocusignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddEsignatureDocusignRequest from a JSON string
add_esignature_docusign_request_instance = AddEsignatureDocusignRequest.from_json(json)
# print the JSON string representation of the object
print AddEsignatureDocusignRequest.to_json()

# convert the object into a dict
add_esignature_docusign_request_dict = add_esignature_docusign_request_instance.to_dict()
# create an instance of AddEsignatureDocusignRequest from a dict
add_esignature_docusign_request_form_dict = add_esignature_docusign_request.from_dict(add_esignature_docusign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


