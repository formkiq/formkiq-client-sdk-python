# WorkflowStepDecision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of Workflow Step Decision | [optional] 
**next_step_id** | **str** | Workflow Step to move to | [optional] 

## Example

```python
from formkiq_client.models.workflow_step_decision import WorkflowStepDecision

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepDecision from a JSON string
workflow_step_decision_instance = WorkflowStepDecision.from_json(json)
# print the JSON string representation of the object
print WorkflowStepDecision.to_json()

# convert the object into a dict
workflow_step_decision_dict = workflow_step_decision_instance.to_dict()
# create an instance of WorkflowStepDecision from a dict
workflow_step_decision_form_dict = workflow_step_decision.from_dict(workflow_step_decision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


