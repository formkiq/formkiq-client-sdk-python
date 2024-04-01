# DocumentWorkflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | Workflow identifier | [optional] 
**name** | **str** | Workflow name | [optional] 
**description** | **str** | Workflow description | [optional] 
**current_step_id** | **str** | The current step workflow is on | [optional] 
**status** | [**DocumentWorkflowStatus**](DocumentWorkflowStatus.md) |  | [optional] 

## Example

```python
from formkiq_client.models.document_workflow import DocumentWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentWorkflow from a JSON string
document_workflow_instance = DocumentWorkflow.from_json(json)
# print the JSON string representation of the object
print(DocumentWorkflow.to_json())

# convert the object into a dict
document_workflow_dict = document_workflow_instance.to_dict()
# create an instance of DocumentWorkflow from a dict
document_workflow_form_dict = document_workflow.from_dict(document_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


