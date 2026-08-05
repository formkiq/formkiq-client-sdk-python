# WorkflowStepConditionAttributeValueComparisonAttribute

Uses another document attribute value as the right-side comparison value. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** | Document attribute key containing the comparison value. | 

## Example

```python
from formkiq_client.models.workflow_step_condition_attribute_value_comparison_attribute import WorkflowStepConditionAttributeValueComparisonAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepConditionAttributeValueComparisonAttribute from a JSON string
workflow_step_condition_attribute_value_comparison_attribute_instance = WorkflowStepConditionAttributeValueComparisonAttribute.from_json(json)
# print the JSON string representation of the object
print(WorkflowStepConditionAttributeValueComparisonAttribute.to_json())

# convert the object into a dict
workflow_step_condition_attribute_value_comparison_attribute_dict = workflow_step_condition_attribute_value_comparison_attribute_instance.to_dict()
# create an instance of WorkflowStepConditionAttributeValueComparisonAttribute from a dict
workflow_step_condition_attribute_value_comparison_attribute_from_dict = WorkflowStepConditionAttributeValueComparisonAttribute.from_dict(workflow_step_condition_attribute_value_comparison_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


