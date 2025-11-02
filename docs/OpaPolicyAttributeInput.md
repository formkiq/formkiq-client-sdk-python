# OpaPolicyAttributeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_username** | **bool** | Match Input Username | [optional] 

## Example

```python
from openapi_client.models.opa_policy_attribute_input import OpaPolicyAttributeInput

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyAttributeInput from a JSON string
opa_policy_attribute_input_instance = OpaPolicyAttributeInput.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyAttributeInput.to_json())

# convert the object into a dict
opa_policy_attribute_input_dict = opa_policy_attribute_input_instance.to_dict()
# create an instance of OpaPolicyAttributeInput from a dict
opa_policy_attribute_input_from_dict = OpaPolicyAttributeInput.from_dict(opa_policy_attribute_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


