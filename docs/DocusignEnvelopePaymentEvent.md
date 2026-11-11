# DocusignEnvelopePaymentEvent

Payment event fields supplied by DocuSign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**actor_display_name** | **str** |  | [optional] 
**event_description** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 
**responsible_actor** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from formkiq_client.models.docusign_envelope_payment_event import DocusignEnvelopePaymentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignEnvelopePaymentEvent from a JSON string
docusign_envelope_payment_event_instance = DocusignEnvelopePaymentEvent.from_json(json)
# print the JSON string representation of the object
print(DocusignEnvelopePaymentEvent.to_json())

# convert the object into a dict
docusign_envelope_payment_event_dict = docusign_envelope_payment_event_instance.to_dict()
# create an instance of DocusignEnvelopePaymentEvent from a dict
docusign_envelope_payment_event_from_dict = DocusignEnvelopePaymentEvent.from_dict(docusign_envelope_payment_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


