# DocusignReminderRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** | Selected DocuSign signer ID from the request | 
**status** | **str** | accepted means DocuSign accepted the reminder request for this recipient, not confirmed delivery. failed means DocuSign returned a definitive recipient-level failure. | 
**message** | **str** | Explanation of a recipient-level failure, when available | [optional] 

## Example

```python
from formkiq_client.models.docusign_reminder_recipient import DocusignReminderRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignReminderRecipient from a JSON string
docusign_reminder_recipient_instance = DocusignReminderRecipient.from_json(json)
# print the JSON string representation of the object
print(DocusignReminderRecipient.to_json())

# convert the object into a dict
docusign_reminder_recipient_dict = docusign_reminder_recipient_instance.to_dict()
# create an instance of DocusignReminderRecipient from a dict
docusign_reminder_recipient_from_dict = DocusignReminderRecipient.from_dict(docusign_reminder_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


