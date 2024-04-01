# GetWorkflowsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**workflows** | [**List[WorkflowSummary]**](WorkflowSummary.md) | List of workflows | [optional] 

## Example

```python
from formkiq_client.models.get_workflows_response import GetWorkflowsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkflowsResponse from a JSON string
get_workflows_response_instance = GetWorkflowsResponse.from_json(json)
# print the JSON string representation of the object
print(GetWorkflowsResponse.to_json())

# convert the object into a dict
get_workflows_response_dict = get_workflows_response_instance.to_dict()
# create an instance of GetWorkflowsResponse from a dict
get_workflows_response_form_dict = get_workflows_response.from_dict(get_workflows_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


