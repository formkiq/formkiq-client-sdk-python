# SystemConfigurationWebUi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sso_automatic_sign_in** | **bool** | Enable SSO automatic sign in | [optional] 

## Example

```python
from formkiq_client.models.system_configuration_web_ui import SystemConfigurationWebUi

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigurationWebUi from a JSON string
system_configuration_web_ui_instance = SystemConfigurationWebUi.from_json(json)
# print the JSON string representation of the object
print(SystemConfigurationWebUi.to_json())

# convert the object into a dict
system_configuration_web_ui_dict = system_configuration_web_ui_instance.to_dict()
# create an instance of SystemConfigurationWebUi from a dict
system_configuration_web_ui_from_dict = SystemConfigurationWebUi.from_dict(system_configuration_web_ui_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


