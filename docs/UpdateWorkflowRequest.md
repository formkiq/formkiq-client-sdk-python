# UpdateWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Workflow name | [optional] 
**description** | **str** | Workflow description | [optional] 
**status** | [**WorkflowStatus**](WorkflowStatus.md) |  | [optional] 

## Example

```python
from openapi_client.model.update_workflow_request import UpdateWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkflowRequest from a JSON string
update_workflow_request_instance = UpdateWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkflowRequest.to_json())

# convert the object into a dict
update_workflow_request_dict = update_workflow_request_instance.to_dict()
# create an instance of UpdateWorkflowRequest from a dict
update_workflow_request_from_dict = UpdateWorkflowRequest.from_dict(update_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


