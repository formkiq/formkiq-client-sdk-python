# SetOpaConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Result message | [optional] 

## Example

```python
from formkiq_client.models.set_opa_configuration_response import SetOpaConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetOpaConfigurationResponse from a JSON string
set_opa_configuration_response_instance = SetOpaConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(SetOpaConfigurationResponse.to_json())

# convert the object into a dict
set_opa_configuration_response_dict = set_opa_configuration_response_instance.to_dict()
# create an instance of SetOpaConfigurationResponse from a dict
set_opa_configuration_response_form_dict = set_opa_configuration_response.from_dict(set_opa_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


