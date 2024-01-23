# UpdateConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Result message | [optional] 

## Example

```python
from formkiq_client.models.update_configuration_response import UpdateConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConfigurationResponse from a JSON string
update_configuration_response_instance = UpdateConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print UpdateConfigurationResponse.to_json()

# convert the object into a dict
update_configuration_response_dict = update_configuration_response_instance.to_dict()
# create an instance of UpdateConfigurationResponse from a dict
update_configuration_response_form_dict = update_configuration_response.from_dict(update_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


