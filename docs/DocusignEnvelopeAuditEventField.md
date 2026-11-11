# DocusignEnvelopeAuditEventField

Field names and values are returned as supplied by DocuSign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**original_value** | **str** |  | [optional] 
**error_details** | [**DocusignEnvelopeAuditEventFieldErrorDetails**](DocusignEnvelopeAuditEventFieldErrorDetails.md) |  | [optional] 

## Example

```python
from formkiq_client.models.docusign_envelope_audit_event_field import DocusignEnvelopeAuditEventField

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignEnvelopeAuditEventField from a JSON string
docusign_envelope_audit_event_field_instance = DocusignEnvelopeAuditEventField.from_json(json)
# print the JSON string representation of the object
print(DocusignEnvelopeAuditEventField.to_json())

# convert the object into a dict
docusign_envelope_audit_event_field_dict = docusign_envelope_audit_event_field_instance.to_dict()
# create an instance of DocusignEnvelopeAuditEventField from a dict
docusign_envelope_audit_event_field_from_dict = DocusignEnvelopeAuditEventField.from_dict(docusign_envelope_audit_event_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


