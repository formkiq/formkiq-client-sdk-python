# OpaPolicyAttributeGt

Attribute greater than criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_value** | **float** | The value to compare the Attribute Key value to | [optional] 

## Example

```python
from openapi_client.model.opa_policy_attribute_gt import OpaPolicyAttributeGt

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyAttributeGt from a JSON string
opa_policy_attribute_gt_instance = OpaPolicyAttributeGt.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyAttributeGt.to_json())

# convert the object into a dict
opa_policy_attribute_gt_dict = opa_policy_attribute_gt_instance.to_dict()
# create an instance of OpaPolicyAttributeGt from a dict
opa_policy_attribute_gt_from_dict = OpaPolicyAttributeGt.from_dict(opa_policy_attribute_gt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


