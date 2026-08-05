# GetSystemConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webui** | [**SystemConfigurationWebUi**](SystemConfigurationWebUi.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_system_configuration_response import GetSystemConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSystemConfigurationResponse from a JSON string
get_system_configuration_response_instance = GetSystemConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(GetSystemConfigurationResponse.to_json())

# convert the object into a dict
get_system_configuration_response_dict = get_system_configuration_response_instance.to_dict()
# create an instance of GetSystemConfigurationResponse from a dict
get_system_configuration_response_from_dict = GetSystemConfigurationResponse.from_dict(get_system_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


