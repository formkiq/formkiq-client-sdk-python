# DocusignInpersonSigner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_email** | **str** | The email of the signing host | 
**host_name** | **str** | The name of the signing host | 
**signer_name** | **str** | The full legal name of a signer | 
**signer_email** | **str** | The in-person signer&#39;s email address | [optional] 
**recipient_id** | **str** | A reference used to map recipients to other objects, such as specific document tabs. | [optional] 
**routing_order** | **str** | Specifies the routing order of the recipient in the envelope. | [optional] 
**suppress_emails** | **str** | When true, email notifications are suppressed for the recipient, and they must access envelopes and documents from their Docusign inbox. | [optional] 
**tabs** | [**DocusignSigningTabs**](DocusignSigningTabs.md) |  | [optional] 

## Example

```python
from openapi_client.model.docusign_inperson_signer import DocusignInpersonSigner

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignInpersonSigner from a JSON string
docusign_inperson_signer_instance = DocusignInpersonSigner.from_json(json)
# print the JSON string representation of the object
print(DocusignInpersonSigner.to_json())

# convert the object into a dict
docusign_inperson_signer_dict = docusign_inperson_signer_instance.to_dict()
# create an instance of DocusignInpersonSigner from a dict
docusign_inperson_signer_from_dict = DocusignInpersonSigner.from_dict(docusign_inperson_signer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


