# WorkflowStepConditionAttributeValueComparisonAggregate

Uses an aggregate over another document attribute's values as the right-side comparison value. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** | Document attribute key whose values are aggregated for comparison. | 
**aggregate_type** | [**WorkflowStepConditionAttributeAggregateType**](WorkflowStepConditionAttributeAggregateType.md) |  | 

## Example

```python
from formkiq_client.models.workflow_step_condition_attribute_value_comparison_aggregate import WorkflowStepConditionAttributeValueComparisonAggregate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepConditionAttributeValueComparisonAggregate from a JSON string
workflow_step_condition_attribute_value_comparison_aggregate_instance = WorkflowStepConditionAttributeValueComparisonAggregate.from_json(json)
# print the JSON string representation of the object
print(WorkflowStepConditionAttributeValueComparisonAggregate.to_json())

# convert the object into a dict
workflow_step_condition_attribute_value_comparison_aggregate_dict = workflow_step_condition_attribute_value_comparison_aggregate_instance.to_dict()
# create an instance of WorkflowStepConditionAttributeValueComparisonAggregate from a dict
workflow_step_condition_attribute_value_comparison_aggregate_from_dict = WorkflowStepConditionAttributeValueComparisonAggregate.from_dict(workflow_step_condition_attribute_value_comparison_aggregate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


