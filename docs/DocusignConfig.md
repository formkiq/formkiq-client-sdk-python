# DocusignConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**DocusignEnvironment**](DocusignEnvironment.md) |  | [optional] 
**user_id** | **str** | Docusign UserId | [optional] 
**integration_key** | **str** | Docusign Integration Key or ClientId | [optional] 
**rsa_private_key** | **str** | Docusign Rsa Private Key | [optional] 
**hmac_signature** | **str** | Optional HMAC secret used to validate Docusign Connect event notifications. When configured, callbacks must include a matching Docusign HMAC signature. When omitted or empty, callbacks are processed without HMAC validation, including when connectUrl is configured. | [optional] 
**connect_url** | **str** | Public HTTPS URL that receives Docusign Connect event notifications. May be configured with or without hmacSignature. | [optional] 

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


