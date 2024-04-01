# SetOpaConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** | OPA Policy in YAML format | [optional] 
**site_id** | **str** | Site Id to apply policy to, leave empty for global policy | [optional] 

## Example

```python
from formkiq_client.models.set_opa_configuration_request import SetOpaConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetOpaConfigurationRequest from a JSON string
set_opa_configuration_request_instance = SetOpaConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(SetOpaConfigurationRequest.to_json())

# convert the object into a dict
set_opa_configuration_request_dict = set_opa_configuration_request_instance.to_dict()
# create an instance of SetOpaConfigurationRequest from a dict
set_opa_configuration_request_form_dict = set_opa_configuration_request.from_dict(set_opa_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


