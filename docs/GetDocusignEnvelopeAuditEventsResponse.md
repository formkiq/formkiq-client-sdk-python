# GetDocusignEnvelopeAuditEventsResponse

DocuSign's envelope audit events response returned unchanged. Additional fields at every level are preserved. Optional collections and fields are returned only when supplied by DocuSign; no events are synthesized.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_events** | [**List[DocusignEnvelopeAuditEvent]**](DocusignEnvelopeAuditEvent.md) | Envelope audit events recorded by DocuSign | [optional] 
**payment_events** | [**List[DocusignEnvelopePaymentEvent]**](DocusignEnvelopePaymentEvent.md) | Payment events returned by DocuSign, when present | [optional] 

## Example

```python
from formkiq_client.models.get_docusign_envelope_audit_events_response import GetDocusignEnvelopeAuditEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocusignEnvelopeAuditEventsResponse from a JSON string
get_docusign_envelope_audit_events_response_instance = GetDocusignEnvelopeAuditEventsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocusignEnvelopeAuditEventsResponse.to_json())

# convert the object into a dict
get_docusign_envelope_audit_events_response_dict = get_docusign_envelope_audit_events_response_instance.to_dict()
# create an instance of GetDocusignEnvelopeAuditEventsResponse from a dict
get_docusign_envelope_audit_events_response_from_dict = GetDocusignEnvelopeAuditEventsResponse.from_dict(get_docusign_envelope_audit_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


