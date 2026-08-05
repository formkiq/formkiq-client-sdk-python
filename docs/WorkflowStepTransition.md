# WorkflowStepTransition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WorkflowStepTransitionType**](WorkflowStepTransitionType.md) |  | 
**step_id** | **str** | Target workflow step | [optional] 

## Example

```python
from formkiq_client.models.workflow_step_transition import WorkflowStepTransition

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepTransition from a JSON string
workflow_step_transition_instance = WorkflowStepTransition.from_json(json)
# print the JSON string representation of the object
print(WorkflowStepTransition.to_json())

# convert the object into a dict
workflow_step_transition_dict = workflow_step_transition_instance.to_dict()
# create an instance of WorkflowStepTransition from a dict
workflow_step_transition_from_dict = WorkflowStepTransition.from_dict(workflow_step_transition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


