# GetDocumentWorkflowsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflows** | [**List[DocumentWorkflow]**](DocumentWorkflow.md) | List of Document Workflows | [optional] 
**next** | **str** |  | [optional] 

## Example

```python
from formkiq_client.models.get_document_workflows_response import GetDocumentWorkflowsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentWorkflowsResponse from a JSON string
get_document_workflows_response_instance = GetDocumentWorkflowsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentWorkflowsResponse.to_json())

# convert the object into a dict
get_document_workflows_response_dict = get_document_workflows_response_instance.to_dict()
# create an instance of GetDocumentWorkflowsResponse from a dict
get_document_workflows_response_from_dict = GetDocumentWorkflowsResponse.from_dict(get_document_workflows_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


