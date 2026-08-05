# WorkflowStepDecisions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WorkflowStepDecisionType**](WorkflowStepDecisionType.md) |  | [optional] 
**next_step_id** | **str** | Workflow Step to move to | [optional] 

## Example

```python
from formkiq_client.models.workflow_step_decisions import WorkflowStepDecisions

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepDecisions from a JSON string
workflow_step_decisions_instance = WorkflowStepDecisions.from_json(json)
# print the JSON string representation of the object
print(WorkflowStepDecisions.to_json())

# convert the object into a dict
workflow_step_decisions_dict = workflow_step_decisions_instance.to_dict()
# create an instance of WorkflowStepDecisions from a dict
workflow_step_decisions_from_dict = WorkflowStepDecisions.from_dict(workflow_step_decisions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


