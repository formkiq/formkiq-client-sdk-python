# VoidDocusignEnvelopeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voided_reason** | **str** | Non-blank, recipient-facing explanation for voiding the DocuSign envelope. At most 200 characters, including spaces and line breaks; longer reasons are rejected without truncation. | 

## Example

```python
from formkiq_client.models.void_docusign_envelope_request import VoidDocusignEnvelopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoidDocusignEnvelopeRequest from a JSON string
void_docusign_envelope_request_instance = VoidDocusignEnvelopeRequest.from_json(json)
# print the JSON string representation of the object
print(VoidDocusignEnvelopeRequest.to_json())

# convert the object into a dict
void_docusign_envelope_request_dict = void_docusign_envelope_request_instance.to_dict()
# create an instance of VoidDocusignEnvelopeRequest from a dict
void_docusign_envelope_request_from_dict = VoidDocusignEnvelopeRequest.from_dict(void_docusign_envelope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


