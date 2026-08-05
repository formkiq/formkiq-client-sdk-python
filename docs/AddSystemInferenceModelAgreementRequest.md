# AddSystemInferenceModelAgreementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** | Bedrock model identifier | 

## Example

```python
from formkiq_client.models.add_system_inference_model_agreement_request import AddSystemInferenceModelAgreementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddSystemInferenceModelAgreementRequest from a JSON string
add_system_inference_model_agreement_request_instance = AddSystemInferenceModelAgreementRequest.from_json(json)
# print the JSON string representation of the object
print(AddSystemInferenceModelAgreementRequest.to_json())

# convert the object into a dict
add_system_inference_model_agreement_request_dict = add_system_inference_model_agreement_request_instance.to_dict()
# create an instance of AddSystemInferenceModelAgreementRequest from a dict
add_system_inference_model_agreement_request_from_dict = AddSystemInferenceModelAgreementRequest.from_dict(add_system_inference_model_agreement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


