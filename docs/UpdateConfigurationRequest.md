# UpdateConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_gpt_api_key** | **str** | ChatGPT Api Key | [optional] 
**max_content_length_bytes** | **str** | Set Maximum Document Content Length in Bytes | [optional] 
**max_documents** | **str** | Set Maximum number of Documents allowed | [optional] 
**max_webhooks** | **str** | Set Maximum number of Webhooks allowed | [optional] 
**notification_email** | **str** | Email address to use for notifications | [optional] 

## Example

```python
from formkiq_client.models.update_configuration_request import UpdateConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConfigurationRequest from a JSON string
update_configuration_request_instance = UpdateConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print UpdateConfigurationRequest.to_json()

# convert the object into a dict
update_configuration_request_dict = update_configuration_request_instance.to_dict()
# create an instance of UpdateConfigurationRequest from a dict
update_configuration_request_form_dict = update_configuration_request.from_dict(update_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


