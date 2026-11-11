# DocusignEnvelopeAuditEvent

Audit event with provider-defined event fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_fields** | [**List[DocusignEnvelopeAuditEventField]**](DocusignEnvelopeAuditEventField.md) |  | [optional] 

## Example

```python
from formkiq_client.models.docusign_envelope_audit_event import DocusignEnvelopeAuditEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignEnvelopeAuditEvent from a JSON string
docusign_envelope_audit_event_instance = DocusignEnvelopeAuditEvent.from_json(json)
# print the JSON string representation of the object
print(DocusignEnvelopeAuditEvent.to_json())

# convert the object into a dict
docusign_envelope_audit_event_dict = docusign_envelope_audit_event_instance.to_dict()
# create an instance of DocusignEnvelopeAuditEvent from a dict
docusign_envelope_audit_event_from_dict = DocusignEnvelopeAuditEvent.from_dict(docusign_envelope_audit_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


