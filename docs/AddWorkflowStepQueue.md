# AddWorkflowStepQueue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queue_id** | **str** | Queue Identifier | 
**approval_groups** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.model.add_workflow_step_queue import AddWorkflowStepQueue

# TODO update the JSON string below
json = "{}"
# create an instance of AddWorkflowStepQueue from a JSON string
add_workflow_step_queue_instance = AddWorkflowStepQueue.from_json(json)
# print the JSON string representation of the object
print(AddWorkflowStepQueue.to_json())

# convert the object into a dict
add_workflow_step_queue_dict = add_workflow_step_queue_instance.to_dict()
# create an instance of AddWorkflowStepQueue from a dict
add_workflow_step_queue_from_dict = AddWorkflowStepQueue.from_dict(add_workflow_step_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


