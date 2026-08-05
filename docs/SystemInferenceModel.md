# SystemInferenceModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**default_model_id** | **str** |  | [optional] 
**model_lifecycle_status** | **str** | Bedrock foundation model lifecycle status. ACTIVE means the model version is available; LEGACY means the model version is deprecated. | [optional] 
**agreement_availability** | **str** |  | [optional] 
**authorization_status** | **str** |  | [optional] 
**entitlement_availability** | **str** |  | [optional] 
**region_availability** | **str** |  | [optional] 
**model_invocations** | [**List[SystemInferenceModelInvocation]**](SystemInferenceModelInvocation.md) |  | [optional] 

## Example

```python
from formkiq_client.models.system_inference_model import SystemInferenceModel

# TODO update the JSON string below
json = "{}"
# create an instance of SystemInferenceModel from a JSON string
system_inference_model_instance = SystemInferenceModel.from_json(json)
# print the JSON string representation of the object
print(SystemInferenceModel.to_json())

# convert the object into a dict
system_inference_model_dict = system_inference_model_instance.to_dict()
# create an instance of SystemInferenceModel from a dict
system_inference_model_from_dict = SystemInferenceModel.from_dict(system_inference_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


