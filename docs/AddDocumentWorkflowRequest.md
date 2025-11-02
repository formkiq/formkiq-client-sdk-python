# AddDocumentWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | Workflow Identifier | 

## Example

```python
from openapi_client.model.add_document_workflow_request import AddDocumentWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentWorkflowRequest from a JSON string
add_document_workflow_request_instance = AddDocumentWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentWorkflowRequest.to_json())

# convert the object into a dict
add_document_workflow_request_dict = add_document_workflow_request_instance.to_dict()
# create an instance of AddDocumentWorkflowRequest from a dict
add_document_workflow_request_from_dict = AddDocumentWorkflowRequest.from_dict(add_document_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


