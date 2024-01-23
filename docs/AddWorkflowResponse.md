# AddWorkflowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | Workflow Identifier | [optional] 

## Example

```python
from formkiq_client.models.add_workflow_response import AddWorkflowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddWorkflowResponse from a JSON string
add_workflow_response_instance = AddWorkflowResponse.from_json(json)
# print the JSON string representation of the object
print AddWorkflowResponse.to_json()

# convert the object into a dict
add_workflow_response_dict = add_workflow_response_instance.to_dict()
# create an instance of AddWorkflowResponse from a dict
add_workflow_response_form_dict = add_workflow_response.from_dict(add_workflow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


