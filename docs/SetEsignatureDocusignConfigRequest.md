# SetEsignatureDocusignConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_key** | **str** | DocuSign App RSA PRIVATE KEY | 
**user_id** | **str** | DocuSign App UserId | 
**client_id** | **str** | DocuSign App Client | 

## Example

```python
from formkiq_client.models.set_esignature_docusign_config_request import SetEsignatureDocusignConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetEsignatureDocusignConfigRequest from a JSON string
set_esignature_docusign_config_request_instance = SetEsignatureDocusignConfigRequest.from_json(json)
# print the JSON string representation of the object
print SetEsignatureDocusignConfigRequest.to_json()

# convert the object into a dict
set_esignature_docusign_config_request_dict = set_esignature_docusign_config_request_instance.to_dict()
# create an instance of SetEsignatureDocusignConfigRequest from a dict
set_esignature_docusign_config_request_form_dict = set_esignature_docusign_config_request.from_dict(set_esignature_docusign_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


