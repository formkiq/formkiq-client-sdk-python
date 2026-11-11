# DocusignEnvelopeAuditEventFieldErrorDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from formkiq_client.models.docusign_envelope_audit_event_field_error_details import DocusignEnvelopeAuditEventFieldErrorDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignEnvelopeAuditEventFieldErrorDetails from a JSON string
docusign_envelope_audit_event_field_error_details_instance = DocusignEnvelopeAuditEventFieldErrorDetails.from_json(json)
# print the JSON string representation of the object
print(DocusignEnvelopeAuditEventFieldErrorDetails.to_json())

# convert the object into a dict
docusign_envelope_audit_event_field_error_details_dict = docusign_envelope_audit_event_field_error_details_instance.to_dict()
# create an instance of DocusignEnvelopeAuditEventFieldErrorDetails from a dict
docusign_envelope_audit_event_field_error_details_from_dict = DocusignEnvelopeAuditEventFieldErrorDetails.from_dict(docusign_envelope_audit_event_field_error_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


