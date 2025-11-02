# DocusignSigner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Signer | 
**email** | **str** | Email of Signer | [optional] 
**client_user_id** | **str** | Specifies unique identifier for signer | [optional] 
**recipient_id** | **str** | A reference used to map recipients to other objects, such as specific document tabs. | [optional] 
**routing_order** | **str** | Specifies the routing order of the recipient in the envelope. | [optional] 
**suppress_emails** | **str** | When true, email notifications are suppressed for the recipient, and they must access envelopes and documents from their Docusign inbox. | [optional] 
**tabs** | [**DocusignSigningTabs**](DocusignSigningTabs.md) |  | [optional] 

## Example

```python
from openapi_client.models.docusign_signer import DocusignSigner

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignSigner from a JSON string
docusign_signer_instance = DocusignSigner.from_json(json)
# print the JSON string representation of the object
print(DocusignSigner.to_json())

# convert the object into a dict
docusign_signer_dict = docusign_signer_instance.to_dict()
# create an instance of DocusignSigner from a dict
docusign_signer_from_dict = DocusignSigner.from_dict(docusign_signer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


