# WorkflowDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow** | [**WorkflowSummary**](WorkflowSummary.md) |  | [optional] 
**document** | [**Document**](Document.md) |  | [optional] 

## Example

```python
from openapi_client.model.workflow_document import WorkflowDocument

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowDocument from a JSON string
workflow_document_instance = WorkflowDocument.from_json(json)
# print the JSON string representation of the object
print(WorkflowDocument.to_json())

# convert the object into a dict
workflow_document_dict = workflow_document_instance.to_dict()
# create an instance of WorkflowDocument from a dict
workflow_document_from_dict = WorkflowDocument.from_dict(workflow_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


