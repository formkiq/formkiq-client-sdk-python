# OpaPolicyTestInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | API Gateway resource template, such as /documents/{documentId}. | 
**http_method** | [**OpaPolicyTestHttpMethod**](OpaPolicyTestHttpMethod.md) |  | 
**path_parameters** | **Dict[str, str]** | Simulated API Gateway path parameters. Defaults to an empty object. | [optional] 
**query_parameters** | **Dict[str, str]** | Simulated API Gateway query parameters. The path siteId is added when siteId is omitted; a different siteId is rejected. | [optional] 
**user** | [**OpaPolicyTestInputUser**](OpaPolicyTestInputUser.md) |  | 

## Example

```python
from formkiq_client.models.opa_policy_test_input import OpaPolicyTestInput

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyTestInput from a JSON string
opa_policy_test_input_instance = OpaPolicyTestInput.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyTestInput.to_json())

# convert the object into a dict
opa_policy_test_input_dict = opa_policy_test_input_instance.to_dict()
# create an instance of OpaPolicyTestInput from a dict
opa_policy_test_input_from_dict = OpaPolicyTestInput.from_dict(opa_policy_test_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


