# DocusignSignerReadyToSignNotification

Configuration for a FormKiQ-managed notification stored with status WAITING when the envelope is created. The Docusign recipient-completed callback for the immediately preceding signer in routing order releases it to PENDING. The callback updates the existing document notification without creating a separate user notification record. The notification is addressed to this signer's email address and does not require suppressEmails to be enabled. Requires a configured connectUrl, unique recipient IDs and unique positive integer routing orders for all signers, and at least one preceding signer. Only sequential signing is supported when readyToSignNotification is configured; parallel routing orders are rejected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_type** | [**DocumentNotificationType**](DocumentNotificationType.md) |  | 
**subject** | **str** | Notification subject | 
**body** | **str** | Notification body | 

## Example

```python
from formkiq_client.models.docusign_signer_ready_to_sign_notification import DocusignSignerReadyToSignNotification

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignSignerReadyToSignNotification from a JSON string
docusign_signer_ready_to_sign_notification_instance = DocusignSignerReadyToSignNotification.from_json(json)
# print the JSON string representation of the object
print(DocusignSignerReadyToSignNotification.to_json())

# convert the object into a dict
docusign_signer_ready_to_sign_notification_dict = docusign_signer_ready_to_sign_notification_instance.to_dict()
# create an instance of DocusignSignerReadyToSignNotification from a dict
docusign_signer_ready_to_sign_notification_from_dict = DocusignSignerReadyToSignNotification.from_dict(docusign_signer_ready_to_sign_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


