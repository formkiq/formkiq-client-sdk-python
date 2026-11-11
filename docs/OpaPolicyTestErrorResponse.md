# OpaPolicyTestErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Sanitized error message. | 
**request_id** | **str** | Request identifier used to locate restricted diagnostic logs. | [optional] 

## Example

```python
from formkiq_client.models.opa_policy_test_error_response import OpaPolicyTestErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyTestErrorResponse from a JSON string
opa_policy_test_error_response_instance = OpaPolicyTestErrorResponse.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyTestErrorResponse.to_json())

# convert the object into a dict
opa_policy_test_error_response_dict = opa_policy_test_error_response_instance.to_dict()
# create an instance of OpaPolicyTestErrorResponse from a dict
opa_policy_test_error_response_from_dict = OpaPolicyTestErrorResponse.from_dict(opa_policy_test_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


