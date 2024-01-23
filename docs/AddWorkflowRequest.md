# AddWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Workflow name | 
**description** | **str** | Workflow description | [optional] 
**status** | **str** |  | 
**steps** | [**List[AddWorkflowStep]**](AddWorkflowStep.md) | Workflow Steps | 

## Example

```python
from formkiq_client.models.add_workflow_request import AddWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddWorkflowRequest from a JSON string
add_workflow_request_instance = AddWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print AddWorkflowRequest.to_json()

# convert the object into a dict
add_workflow_request_dict = add_workflow_request_instance.to_dict()
# create an instance of AddWorkflowRequest from a dict
add_workflow_request_form_dict = add_workflow_request.from_dict(add_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


