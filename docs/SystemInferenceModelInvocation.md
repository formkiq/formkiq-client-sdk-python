# SystemInferenceModelInvocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** |  | 
**invocation_type** | **str** |  | 
**inference_profile_type** | **str** |  | [optional] 
**geo** | **str** |  | [optional] 

## Example

```python
from formkiq_client.models.system_inference_model_invocation import SystemInferenceModelInvocation

# TODO update the JSON string below
json = "{}"
# create an instance of SystemInferenceModelInvocation from a JSON string
system_inference_model_invocation_instance = SystemInferenceModelInvocation.from_json(json)
# print the JSON string representation of the object
print(SystemInferenceModelInvocation.to_json())

# convert the object into a dict
system_inference_model_invocation_dict = system_inference_model_invocation_instance.to_dict()
# create an instance of SystemInferenceModelInvocation from a dict
system_inference_model_invocation_from_dict = SystemInferenceModelInvocation.from_dict(system_inference_model_invocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


