# DeleteWorkflowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Result message | [optional] 

## Example

```python
from formkiq_client.models.delete_workflow_response import DeleteWorkflowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWorkflowResponse from a JSON string
delete_workflow_response_instance = DeleteWorkflowResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteWorkflowResponse.to_json())

# convert the object into a dict
delete_workflow_response_dict = delete_workflow_response_instance.to_dict()
# create an instance of DeleteWorkflowResponse from a dict
delete_workflow_response_form_dict = delete_workflow_response.from_dict(delete_workflow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


