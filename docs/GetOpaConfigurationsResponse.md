# GetOpaConfigurationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**opa_policies** | [**List[OpaPolicy]**](OpaPolicy.md) | List of OPA policies | [optional] 

## Example

```python
from formkiq_client.models.get_opa_configurations_response import GetOpaConfigurationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpaConfigurationsResponse from a JSON string
get_opa_configurations_response_instance = GetOpaConfigurationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetOpaConfigurationsResponse.to_json())

# convert the object into a dict
get_opa_configurations_response_dict = get_opa_configurations_response_instance.to_dict()
# create an instance of GetOpaConfigurationsResponse from a dict
get_opa_configurations_response_form_dict = get_opa_configurations_response.from_dict(get_opa_configurations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


