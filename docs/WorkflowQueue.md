# WorkflowQueue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queue_id** | **str** | Queue Id | [optional] 
**approval_groups** | **List[str]** |  | [optional] 

## Example

```python
from formkiq_client.models.workflow_queue import WorkflowQueue

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowQueue from a JSON string
workflow_queue_instance = WorkflowQueue.from_json(json)
# print the JSON string representation of the object
print(WorkflowQueue.to_json())

# convert the object into a dict
workflow_queue_dict = workflow_queue_instance.to_dict()
# create an instance of WorkflowQueue from a dict
workflow_queue_form_dict = workflow_queue.from_dict(workflow_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


