# WorkflowStepCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | [**List[WorkflowStepConditionCriterion]**](WorkflowStepConditionCriterion.md) | Workflow Step Condition Criteria | [optional] 
**any** | [**List[WorkflowStepConditionCriterion]**](WorkflowStepConditionCriterion.md) | Workflow Step Condition Criteria | [optional] 
**transition** | [**WorkflowStepTransition**](WorkflowStepTransition.md) |  | 

## Example

```python
from formkiq_client.models.workflow_step_condition import WorkflowStepCondition

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepCondition from a JSON string
workflow_step_condition_instance = WorkflowStepCondition.from_json(json)
# print the JSON string representation of the object
print(WorkflowStepCondition.to_json())

# convert the object into a dict
workflow_step_condition_dict = workflow_step_condition_instance.to_dict()
# create an instance of WorkflowStepCondition from a dict
workflow_step_condition_from_dict = WorkflowStepCondition.from_dict(workflow_step_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


