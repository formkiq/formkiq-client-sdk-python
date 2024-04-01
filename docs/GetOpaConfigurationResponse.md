# GetOpaConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opa_policy** | [**OpaPolicy**](OpaPolicy.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_opa_configuration_response import GetOpaConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpaConfigurationResponse from a JSON string
get_opa_configuration_response_instance = GetOpaConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(GetOpaConfigurationResponse.to_json())

# convert the object into a dict
get_opa_configuration_response_dict = get_opa_configuration_response_instance.to_dict()
# create an instance of GetOpaConfigurationResponse from a dict
get_opa_configuration_response_form_dict = get_opa_configuration_response.from_dict(get_opa_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


