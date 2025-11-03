# GetWorkflowQueueDocumentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**documents** | [**List[WorkflowDocument]**](WorkflowDocument.md) | List of search result documents | [optional] 

## Example

```python
from formkiq_client.models.get_workflow_queue_documents_response import GetWorkflowQueueDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkflowQueueDocumentsResponse from a JSON string
get_workflow_queue_documents_response_instance = GetWorkflowQueueDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print(GetWorkflowQueueDocumentsResponse.to_json())

# convert the object into a dict
get_workflow_queue_documents_response_dict = get_workflow_queue_documents_response_instance.to_dict()
# create an instance of GetWorkflowQueueDocumentsResponse from a dict
get_workflow_queue_documents_response_from_dict = GetWorkflowQueueDocumentsResponse.from_dict(get_workflow_queue_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


