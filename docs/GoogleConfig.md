# GoogleConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workload_identity_audience** | **str** | Workload Identity Audience | [optional] 
**workload_identity_service_account** | **str** | Workload Service Account | [optional] 

## Example

```python
from openapi_client.model.google_config import GoogleConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleConfig from a JSON string
google_config_instance = GoogleConfig.from_json(json)
# print the JSON string representation of the object
print(GoogleConfig.to_json())

# convert the object into a dict
google_config_dict = google_config_instance.to_dict()
# create an instance of GoogleConfig from a dict
google_config_from_dict = GoogleConfig.from_dict(google_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


