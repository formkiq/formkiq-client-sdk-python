# WorkflowStepConditionAttributeValueComparisonTarget

Defines the right-side comparison value for an attribute value comparison. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** | Document attribute key whose values are aggregated for comparison. | 
**aggregate_type** | [**WorkflowStepConditionAttributeAggregateType**](WorkflowStepConditionAttributeAggregateType.md) |  | 

## Example

```python
from formkiq_client.models.workflow_step_condition_attribute_value_comparison_target import WorkflowStepConditionAttributeValueComparisonTarget

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepConditionAttributeValueComparisonTarget from a JSON string
workflow_step_condition_attribute_value_comparison_target_instance = WorkflowStepConditionAttributeValueComparisonTarget.from_json(json)
# print the JSON string representation of the object
print(WorkflowStepConditionAttributeValueComparisonTarget.to_json())

# convert the object into a dict
workflow_step_condition_attribute_value_comparison_target_dict = workflow_step_condition_attribute_value_comparison_target_instance.to_dict()
# create an instance of WorkflowStepConditionAttributeValueComparisonTarget from a dict
workflow_step_condition_attribute_value_comparison_target_from_dict = WorkflowStepConditionAttributeValueComparisonTarget.from_dict(workflow_step_condition_attribute_value_comparison_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


