# GetSystemInferenceModelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inference_models** | [**List[SystemInferenceModel]**](SystemInferenceModel.md) | List of system inference models | [optional] 

## Example

```python
from formkiq_client.models.get_system_inference_models_response import GetSystemInferenceModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSystemInferenceModelsResponse from a JSON string
get_system_inference_models_response_instance = GetSystemInferenceModelsResponse.from_json(json)
# print the JSON string representation of the object
print(GetSystemInferenceModelsResponse.to_json())

# convert the object into a dict
get_system_inference_models_response_dict = get_system_inference_models_response_instance.to_dict()
# create an instance of GetSystemInferenceModelsResponse from a dict
get_system_inference_models_response_from_dict = GetSystemInferenceModelsResponse.from_dict(get_system_inference_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


