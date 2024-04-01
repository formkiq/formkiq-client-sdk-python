# GetDocumentWorkflowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow** | [**DocumentWorkflow**](DocumentWorkflow.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_document_workflow_response import GetDocumentWorkflowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentWorkflowResponse from a JSON string
get_document_workflow_response_instance = GetDocumentWorkflowResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentWorkflowResponse.to_json())

# convert the object into a dict
get_document_workflow_response_dict = get_document_workflow_response_instance.to_dict()
# create an instance of GetDocumentWorkflowResponse from a dict
get_document_workflow_response_form_dict = get_document_workflow_response.from_dict(get_document_workflow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


