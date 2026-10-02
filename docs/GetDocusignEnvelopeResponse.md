# GetDocusignEnvelopeResponse

The DocuSign Get Envelope response with include=recipients, returned without enrichment. Additional DocuSign fields are preserved. Optional fields are returned only when supplied by DocuSign. A completed envelope does not confirm that FormKiQ has stored the signed PDF.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**envelope_id** | **str** | DocuSign envelope identifier | [optional] 
**status** | **str** | Envelope status reported by DocuSign, such as created, sent, delivered, signed, completed, declined, or voided. | [optional] 
**status_changed_date_time** | **datetime** | Time DocuSign reports the envelope status changed | [optional] 
**sent_date_time** | **datetime** |  | [optional] 
**delivered_date_time** | **datetime** |  | [optional] 
**completed_date_time** | **datetime** |  | [optional] 
**declined_date_time** | **datetime** |  | [optional] 
**voided_date_time** | **datetime** |  | [optional] 
**recipients** | [**DocusignEnvelopeRecipients**](DocusignEnvelopeRecipients.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_docusign_envelope_response import GetDocusignEnvelopeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocusignEnvelopeResponse from a JSON string
get_docusign_envelope_response_instance = GetDocusignEnvelopeResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocusignEnvelopeResponse.to_json())

# convert the object into a dict
get_docusign_envelope_response_dict = get_docusign_envelope_response_instance.to_dict()
# create an instance of GetDocusignEnvelopeResponse from a dict
get_docusign_envelope_response_from_dict = GetDocusignEnvelopeResponse.from_dict(get_docusign_envelope_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


