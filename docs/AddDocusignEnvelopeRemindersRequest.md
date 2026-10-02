# AddDocusignEnvelopeRemindersRequest

Optional selection of one or more signers. Omit the body or send an empty object to remind all eligible recipients at the current routing step. The singular recipientId field, signer names, and email addresses are not accepted. Invalid selections never trigger an envelope-level reminder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_ids** | **List[str]** | Existing DocuSign signer IDs from recipients.signers[].recipientId in GET /esignature/docusign/{documentId}/envelopes/{envelopeId} for this same envelope. Every selected signer must be notification-eligible and awaiting action at the current routing step. Validate the entire selection before issuing a resend. Null or empty arrays, duplicate IDs, and null, empty, whitespace-only, or non-string entries are invalid. Omit this property for an envelope-level reminder. | [optional] 

## Example

```python
from formkiq_client.models.add_docusign_envelope_reminders_request import AddDocusignEnvelopeRemindersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocusignEnvelopeRemindersRequest from a JSON string
add_docusign_envelope_reminders_request_instance = AddDocusignEnvelopeRemindersRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocusignEnvelopeRemindersRequest.to_json())

# convert the object into a dict
add_docusign_envelope_reminders_request_dict = add_docusign_envelope_reminders_request_instance.to_dict()
# create an instance of AddDocusignEnvelopeRemindersRequest from a dict
add_docusign_envelope_reminders_request_from_dict = AddDocusignEnvelopeRemindersRequest.from_dict(add_docusign_envelope_reminders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


