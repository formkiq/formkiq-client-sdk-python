# GetWorkflowDocumentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**documents** | [**List[Document]**](Document.md) | List of workflow documents | [optional] 

## Example

```python
from formkiq_client.models.get_workflow_documents_response import GetWorkflowDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkflowDocumentsResponse from a JSON string
get_workflow_documents_response_instance = GetWorkflowDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print GetWorkflowDocumentsResponse.to_json()

# convert the object into a dict
get_workflow_documents_response_dict = get_workflow_documents_response_instance.to_dict()
# create an instance of GetWorkflowDocumentsResponse from a dict
get_workflow_documents_response_form_dict = get_workflow_documents_response.from_dict(get_workflow_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


