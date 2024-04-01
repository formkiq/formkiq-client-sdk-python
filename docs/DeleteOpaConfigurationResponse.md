# DeleteOpaConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Result message | [optional] 

## Example

```python
from formkiq_client.models.delete_opa_configuration_response import DeleteOpaConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOpaConfigurationResponse from a JSON string
delete_opa_configuration_response_instance = DeleteOpaConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteOpaConfigurationResponse.to_json())

# convert the object into a dict
delete_opa_configuration_response_dict = delete_opa_configuration_response_instance.to_dict()
# create an instance of DeleteOpaConfigurationResponse from a dict
delete_opa_configuration_response_form_dict = delete_opa_configuration_response.from_dict(delete_opa_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


