# GetWorkflowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Workflow name | [optional] 
**description** | **str** | Workflow description | [optional] 
**in_use** | **bool** | Whether the Workflow is in use | [optional] 
**status** | **str** |  | [optional] 
**steps** | [**List[WorkflowStep]**](WorkflowStep.md) | Workflow steps | [optional] 

## Example

```python
from formkiq_client.models.get_workflow_response import GetWorkflowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkflowResponse from a JSON string
get_workflow_response_instance = GetWorkflowResponse.from_json(json)
# print the JSON string representation of the object
print GetWorkflowResponse.to_json()

# convert the object into a dict
get_workflow_response_dict = get_workflow_response_instance.to_dict()
# create an instance of GetWorkflowResponse from a dict
get_workflow_response_form_dict = get_workflow_response.from_dict(get_workflow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


