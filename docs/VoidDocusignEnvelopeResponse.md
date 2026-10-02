# VoidDocusignEnvelopeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**envelope_id** | **str** | Identifier of the DocuSign envelope that was voided | 
**status** | **str** | Envelope status after the successful operation, voided | 

## Example

```python
from formkiq_client.models.void_docusign_envelope_response import VoidDocusignEnvelopeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoidDocusignEnvelopeResponse from a JSON string
void_docusign_envelope_response_instance = VoidDocusignEnvelopeResponse.from_json(json)
# print the JSON string representation of the object
print(VoidDocusignEnvelopeResponse.to_json())

# convert the object into a dict
void_docusign_envelope_response_dict = void_docusign_envelope_response_instance.to_dict()
# create an instance of VoidDocusignEnvelopeResponse from a dict
void_docusign_envelope_response_from_dict = VoidDocusignEnvelopeResponse.from_dict(void_docusign_envelope_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


