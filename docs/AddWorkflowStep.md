# AddWorkflowStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_id** | **str** | Workflow Step Identifier | [optional] 
**description** | **str** | Workflow Step description | [optional] 
**action** | [**AddAction**](AddAction.md) |  | [optional] 
**queue** | [**AddWorkflowStepQueue**](AddWorkflowStepQueue.md) |  | [optional] 
**mappings** | [**List[WorkflowStepMapping]**](WorkflowStepMapping.md) |  | [optional] 
**decision** | [**WorkflowStepDecision**](WorkflowStepDecision.md) |  | [optional] 
**decisions** | [**List[AddWorkflowStepDecision]**](AddWorkflowStepDecision.md) | Deprecated; use &#39;decision&#39; instead | [optional] 

## Example

```python
from formkiq_client.models.add_workflow_step import AddWorkflowStep

# TODO update the JSON string below
json = "{}"
# create an instance of AddWorkflowStep from a JSON string
add_workflow_step_instance = AddWorkflowStep.from_json(json)
# print the JSON string representation of the object
print(AddWorkflowStep.to_json())

# convert the object into a dict
add_workflow_step_dict = add_workflow_step_instance.to_dict()
# create an instance of AddWorkflowStep from a dict
add_workflow_step_from_dict = AddWorkflowStep.from_dict(add_workflow_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


