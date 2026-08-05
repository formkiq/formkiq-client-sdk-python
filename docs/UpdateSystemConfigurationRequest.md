# UpdateSystemConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webui** | [**SystemConfigurationWebUi**](SystemConfigurationWebUi.md) |  | [optional] 

## Example

```python
from formkiq_client.models.update_system_configuration_request import UpdateSystemConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSystemConfigurationRequest from a JSON string
update_system_configuration_request_instance = UpdateSystemConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSystemConfigurationRequest.to_json())

# convert the object into a dict
update_system_configuration_request_dict = update_system_configuration_request_instance.to_dict()
# create an instance of UpdateSystemConfigurationRequest from a dict
update_system_configuration_request_from_dict = UpdateSystemConfigurationRequest.from_dict(update_system_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


