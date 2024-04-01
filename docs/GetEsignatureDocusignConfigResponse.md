# GetEsignatureDocusignConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configured** | **bool** | Whether DocuSign is configured | [optional] 
**user_id** | **str** | DocuSign UserId configured | [optional] 
**client_id** | **str** | DocuSign Client configured | [optional] 

## Example

```python
from formkiq_client.models.get_esignature_docusign_config_response import GetEsignatureDocusignConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEsignatureDocusignConfigResponse from a JSON string
get_esignature_docusign_config_response_instance = GetEsignatureDocusignConfigResponse.from_json(json)
# print the JSON string representation of the object
print(GetEsignatureDocusignConfigResponse.to_json())

# convert the object into a dict
get_esignature_docusign_config_response_dict = get_esignature_docusign_config_response_instance.to_dict()
# create an instance of GetEsignatureDocusignConfigResponse from a dict
get_esignature_docusign_config_response_form_dict = get_esignature_docusign_config_response.from_dict(get_esignature_docusign_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


