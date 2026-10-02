# AddDocusignEnvelopeRemindersResponse

For targeted reminders, recipients contains exactly one outcome for each requested recipient ID. HTTP 200 can include accepted and failed outcomes, including when every recipient failed at the provider after validation. Invalid selections detected before the resend return 400 instead. Envelope-wide acceptance returns an empty object; do not infer individual outcomes. There is no overall status field. Authentication, validation, rate-limit, upstream, and timeout errors use the documented 4xx/5xx responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | [**List[DocusignReminderRecipient]**](DocusignReminderRecipient.md) | Outcomes for the selected recipients, present for targeted requests and omitted for envelope-wide reminders. A timeout or missing provider outcome must not be represented as confirmed acceptance or failure. | [optional] 

## Example

```python
from formkiq_client.models.add_docusign_envelope_reminders_response import AddDocusignEnvelopeRemindersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocusignEnvelopeRemindersResponse from a JSON string
add_docusign_envelope_reminders_response_instance = AddDocusignEnvelopeRemindersResponse.from_json(json)
# print the JSON string representation of the object
print(AddDocusignEnvelopeRemindersResponse.to_json())

# convert the object into a dict
add_docusign_envelope_reminders_response_dict = add_docusign_envelope_reminders_response_instance.to_dict()
# create an instance of AddDocusignEnvelopeRemindersResponse from a dict
add_docusign_envelope_reminders_response_from_dict = AddDocusignEnvelopeRemindersResponse.from_dict(add_docusign_envelope_reminders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


