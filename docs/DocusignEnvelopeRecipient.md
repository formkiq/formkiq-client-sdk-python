# DocusignEnvelopeRecipient

Recipient fields returned by DocuSign. Fields depend on the recipient type; additional type-specific fields are preserved. This response schema is separate from FormKiQ's envelope creation request schemas.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** |  | [optional] 
**recipient_id_guid** | **str** |  | [optional] 
**recipient_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**signer_name** | **str** |  | [optional] 
**signer_email** | **str** |  | [optional] 
**host_name** | **str** |  | [optional] 
**host_email** | **str** |  | [optional] 
**routing_order** | **str** |  | [optional] 
**status** | **str** | Recipient status reported by DocuSign | [optional] 
**sent_date_time** | **datetime** |  | [optional] 
**delivered_date_time** | **datetime** |  | [optional] 
**signed_date_time** | **datetime** |  | [optional] 
**declined_date_time** | **datetime** |  | [optional] 

## Example

```python
from formkiq_client.models.docusign_envelope_recipient import DocusignEnvelopeRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignEnvelopeRecipient from a JSON string
docusign_envelope_recipient_instance = DocusignEnvelopeRecipient.from_json(json)
# print the JSON string representation of the object
print(DocusignEnvelopeRecipient.to_json())

# convert the object into a dict
docusign_envelope_recipient_dict = docusign_envelope_recipient_instance.to_dict()
# create an instance of DocusignEnvelopeRecipient from a dict
docusign_envelope_recipient_from_dict = DocusignEnvelopeRecipient.from_dict(docusign_envelope_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


