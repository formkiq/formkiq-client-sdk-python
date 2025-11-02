# AddDocusignEnvelopesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_subject** | **str** | The subject line of the email message that is sent to all recipients | [optional] 
**environment** | [**DocusignEnvironment**](DocusignEnvironment.md) |  | 
**signers** | [**List[DocusignSigner]**](DocusignSigner.md) | List of DocuSign Signers | [optional] 
**inperson_signers** | [**List[DocusignInpersonSigner]**](DocusignInpersonSigner.md) | List of DocuSign Inperson Signers | [optional] 
**notification** | [**DocusignNotification**](DocusignNotification.md) |  | [optional] 

## Example

```python
from openapi_client.models.add_docusign_envelopes_request import AddDocusignEnvelopesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocusignEnvelopesRequest from a JSON string
add_docusign_envelopes_request_instance = AddDocusignEnvelopesRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocusignEnvelopesRequest.to_json())

# convert the object into a dict
add_docusign_envelopes_request_dict = add_docusign_envelopes_request_instance.to_dict()
# create an instance of AddDocusignEnvelopesRequest from a dict
add_docusign_envelopes_request_from_dict = AddDocusignEnvelopesRequest.from_dict(add_docusign_envelopes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


