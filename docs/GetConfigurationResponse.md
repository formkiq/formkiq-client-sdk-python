# GetConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_gpt_api_key** | **str** | ChatGPT API Key | [optional] 
**max_content_length_bytes** | **str** | Set Maximum Document Content Length in Bytes | [optional] 
**max_documents** | **str** | Set Maximum number of Documents allowed | [optional] 
**max_webhooks** | **str** | Set Maximum number of Webhooks allowed | [optional] 
**notification_email** | **str** | Email address to use for notifications (Must be verified identity created in AWS SES) | [optional] 

## Example

```python
from formkiq_client.models.get_configuration_response import GetConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetConfigurationResponse from a JSON string
get_configuration_response_instance = GetConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print GetConfigurationResponse.to_json()

# convert the object into a dict
get_configuration_response_dict = get_configuration_response_instance.to_dict()
# create an instance of GetConfigurationResponse from a dict
get_configuration_response_form_dict = get_configuration_response.from_dict(get_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


