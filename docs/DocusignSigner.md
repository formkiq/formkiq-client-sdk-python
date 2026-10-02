# DocusignSigner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Signer | 
**email** | **str** | Email of Signer | [optional] 
**client_user_id** | **str** | Specifies unique identifier for signer | [optional] 
**embedded_recipient_start_url** | **str** | Enables a Docusign signing invitation while retaining embedded signing through clientUserId. Requires clientUserId. When omitted, the existing signing behavior is unchanged. Hybrid recipients do not receive automated reminders or expiration notifications. | [optional] 
**recipient_id** | **str** | A reference used to map recipients to other objects, such as specific document tabs. | [optional] 
**routing_order** | **str** | Specifies the routing order of the recipient in the envelope. | [optional] 
**suppress_emails** | **str** | When true, email notifications are suppressed for the recipient, and they must access envelopes and documents from their Docusign inbox. | [optional] 
**ready_to_sign_notification** | [**DocusignSignerReadyToSignNotification**](DocusignSignerReadyToSignNotification.md) |  | [optional] 
**tabs** | [**DocusignSigningTabs**](DocusignSigningTabs.md) |  | [optional] 

## Example

```python
from formkiq_client.models.docusign_signer import DocusignSigner

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignSigner from a JSON string
docusign_signer_instance = DocusignSigner.from_json(json)
# print the JSON string representation of the object
print(DocusignSigner.to_json())

# convert the object into a dict
docusign_signer_dict = docusign_signer_instance.to_dict()
# create an instance of DocusignSigner from a dict
docusign_signer_from_dict = DocusignSigner.from_dict(docusign_signer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


