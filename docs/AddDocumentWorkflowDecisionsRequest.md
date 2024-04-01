# AddDocumentWorkflowDecisionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_id** | **str** | Workflow Step Identifier | [optional] 
**comments** | **str** | Workflow decision comments | [optional] 
**decision** | **str** |  | 

## Example

```python
from formkiq_client.models.add_document_workflow_decisions_request import AddDocumentWorkflowDecisionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentWorkflowDecisionsRequest from a JSON string
add_document_workflow_decisions_request_instance = AddDocumentWorkflowDecisionsRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentWorkflowDecisionsRequest.to_json())

# convert the object into a dict
add_document_workflow_decisions_request_dict = add_document_workflow_decisions_request_instance.to_dict()
# create an instance of AddDocumentWorkflowDecisionsRequest from a dict
add_document_workflow_decisions_request_form_dict = add_document_workflow_decisions_request.from_dict(add_document_workflow_decisions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


