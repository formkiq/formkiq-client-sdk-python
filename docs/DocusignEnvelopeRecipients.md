# DocusignEnvelopeRecipients

Recipient information returned by DocuSign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_count** | **str** | Number of recipients, represented as a DocuSign string | [optional] 
**current_routing_order** | **str** | Current routing step. Match this to recipient routingOrder and inspect recipient status to identify outstanding actions. Multiple recipients can share a routing order. Also check envelope status before treating a recipient as awaiting action. | [optional] 
**signers** | [**List[DocusignEnvelopeRecipient]**](DocusignEnvelopeRecipient.md) |  | [optional] 
**in_person_signers** | [**List[DocusignEnvelopeRecipient]**](DocusignEnvelopeRecipient.md) |  | [optional] 
**agents** | [**List[DocusignEnvelopeRecipient]**](DocusignEnvelopeRecipient.md) |  | [optional] 
**editors** | [**List[DocusignEnvelopeRecipient]**](DocusignEnvelopeRecipient.md) |  | [optional] 
**intermediaries** | [**List[DocusignEnvelopeRecipient]**](DocusignEnvelopeRecipient.md) |  | [optional] 
**carbon_copies** | [**List[DocusignEnvelopeRecipient]**](DocusignEnvelopeRecipient.md) |  | [optional] 
**certified_deliveries** | [**List[DocusignEnvelopeRecipient]**](DocusignEnvelopeRecipient.md) |  | [optional] 
**witnesses** | [**List[DocusignEnvelopeRecipient]**](DocusignEnvelopeRecipient.md) |  | [optional] 
**seals** | [**List[DocusignEnvelopeRecipient]**](DocusignEnvelopeRecipient.md) |  | [optional] 
**notaries** | [**List[DocusignEnvelopeRecipient]**](DocusignEnvelopeRecipient.md) |  | [optional] 

## Example

```python
from formkiq_client.models.docusign_envelope_recipients import DocusignEnvelopeRecipients

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignEnvelopeRecipients from a JSON string
docusign_envelope_recipients_instance = DocusignEnvelopeRecipients.from_json(json)
# print the JSON string representation of the object
print(DocusignEnvelopeRecipients.to_json())

# convert the object into a dict
docusign_envelope_recipients_dict = docusign_envelope_recipients_instance.to_dict()
# create an instance of DocusignEnvelopeRecipients from a dict
docusign_envelope_recipients_from_dict = DocusignEnvelopeRecipients.from_dict(docusign_envelope_recipients_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


