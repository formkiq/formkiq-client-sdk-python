# AddDocusignEnvelopesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**envelope_id** | **str** | Docusign Envelope Identifier | [optional] 

## Example

```python
from formkiq_client.models.add_docusign_envelopes_response import AddDocusignEnvelopesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocusignEnvelopesResponse from a JSON string
add_docusign_envelopes_response_instance = AddDocusignEnvelopesResponse.from_json(json)
# print the JSON string representation of the object
print(AddDocusignEnvelopesResponse.to_json())

# convert the object into a dict
add_docusign_envelopes_response_dict = add_docusign_envelopes_response_instance.to_dict()
# create an instance of AddDocusignEnvelopesResponse from a dict
add_docusign_envelopes_response_from_dict = AddDocusignEnvelopesResponse.from_dict(add_docusign_envelopes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


