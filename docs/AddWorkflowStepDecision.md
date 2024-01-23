# AddWorkflowStepDecision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of Workflow Step Decision | 
**next_step_id** | **str** | Workflow Step to move to | 

## Example

```python
from formkiq_client.models.add_workflow_step_decision import AddWorkflowStepDecision

# TODO update the JSON string below
json = "{}"
# create an instance of AddWorkflowStepDecision from a JSON string
add_workflow_step_decision_instance = AddWorkflowStepDecision.from_json(json)
# print the JSON string representation of the object
print AddWorkflowStepDecision.to_json()

# convert the object into a dict
add_workflow_step_decision_dict = add_workflow_step_decision_instance.to_dict()
# create an instance of AddWorkflowStepDecision from a dict
add_workflow_step_decision_form_dict = add_workflow_step_decision.from_dict(add_workflow_step_decision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


