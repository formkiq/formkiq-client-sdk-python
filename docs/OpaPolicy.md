# OpaPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **str** | SiteId to apply OPA Policy to | [optional] 
**policy** | **str** | OPA Policy in REGO format | [optional] 

## Example

```python
from openapi_client.models.opa_policy import OpaPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicy from a JSON string
opa_policy_instance = OpaPolicy.from_json(json)
# print the JSON string representation of the object
print(OpaPolicy.to_json())

# convert the object into a dict
opa_policy_dict = opa_policy_instance.to_dict()
# create an instance of OpaPolicy from a dict
opa_policy_from_dict = OpaPolicy.from_dict(opa_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


