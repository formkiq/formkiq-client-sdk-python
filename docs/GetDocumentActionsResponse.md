# GetDocumentActionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**actions** | [**List[DocumentAction]**](DocumentAction.md) | List of document actions | [optional] 

## Example

```python
from openapi_client.models.get_document_actions_response import GetDocumentActionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentActionsResponse from a JSON string
get_document_actions_response_instance = GetDocumentActionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentActionsResponse.to_json())

# convert the object into a dict
get_document_actions_response_dict = get_document_actions_response_instance.to_dict()
# create an instance of GetDocumentActionsResponse from a dict
get_document_actions_response_from_dict = GetDocumentActionsResponse.from_dict(get_document_actions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


