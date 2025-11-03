# DocusignConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Docusign UserId | [optional] 
**integration_key** | **str** | Docusign Integration Key or ClientId | [optional] 
**rsa_private_key** | **str** | Docusign Rsa Private Key | [optional] 
**hmac_signature** | **str** | Enabled security with Docusign Connect using HMAC keys. When enabled these keys are known only by Docusign and your app, and will be used to sign all Connect messages sent from your Docusign account to your application. | [optional] 

## Example

```python
from formkiq_client.models.docusign_config import DocusignConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignConfig from a JSON string
docusign_config_instance = DocusignConfig.from_json(json)
# print the JSON string representation of the object
print(DocusignConfig.to_json())

# convert the object into a dict
docusign_config_dict = docusign_config_instance.to_dict()
# create an instance of DocusignConfig from a dict
docusign_config_from_dict = DocusignConfig.from_dict(docusign_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


