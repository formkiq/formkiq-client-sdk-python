# EsignatureDocusignSigner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Signer | [optional] 
**email** | **str** | Email of Signer | [optional] 

## Example

```python
from formkiq_client.models.esignature_docusign_signer import EsignatureDocusignSigner

# TODO update the JSON string below
json = "{}"
# create an instance of EsignatureDocusignSigner from a JSON string
esignature_docusign_signer_instance = EsignatureDocusignSigner.from_json(json)
# print the JSON string representation of the object
print(EsignatureDocusignSigner.to_json())

# convert the object into a dict
esignature_docusign_signer_dict = esignature_docusign_signer_instance.to_dict()
# create an instance of EsignatureDocusignSigner from a dict
esignature_docusign_signer_from_dict = EsignatureDocusignSigner.from_dict(esignature_docusign_signer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


