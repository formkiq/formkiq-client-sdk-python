# WorkflowStepConditionAttributeValueComparison

Compares the value of one document attribute to another attribute-derived value on the same document.  The criterion operator is evaluated as: document.attribute[valueAttributeKey] OP comparison  Literal comparison value fields are not used with this source. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**WorkflowStepConditionAttributeValueComparisonSourceType**](WorkflowStepConditionAttributeValueComparisonSourceType.md) |  | 
**value_attribute_key** | **str** | Document attribute key containing the value to compare. | 
**comparison** | [**WorkflowStepConditionAttributeValueComparisonTarget**](WorkflowStepConditionAttributeValueComparisonTarget.md) |  | 

## Example

```python
from formkiq_client.models.workflow_step_condition_attribute_value_comparison import WorkflowStepConditionAttributeValueComparison

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepConditionAttributeValueComparison from a JSON string
workflow_step_condition_attribute_value_comparison_instance = WorkflowStepConditionAttributeValueComparison.from_json(json)
# print the JSON string representation of the object
print(WorkflowStepConditionAttributeValueComparison.to_json())

# convert the object into a dict
workflow_step_condition_attribute_value_comparison_dict = workflow_step_condition_attribute_value_comparison_instance.to_dict()
# create an instance of WorkflowStepConditionAttributeValueComparison from a dict
workflow_step_condition_attribute_value_comparison_from_dict = WorkflowStepConditionAttributeValueComparison.from_dict(workflow_step_condition_attribute_value_comparison_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


