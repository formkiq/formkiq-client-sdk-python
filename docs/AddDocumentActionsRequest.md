# AddDocumentActionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[AddAction]**](AddAction.md) | List of Actions | [optional] 

## Example

```python
from openapi_client.models.add_document_actions_request import AddDocumentActionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentActionsRequest from a JSON string
add_document_actions_request_instance = AddDocumentActionsRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentActionsRequest.to_json())

# convert the object into a dict
add_document_actions_request_dict = add_document_actions_request_instance.to_dict()
# create an instance of AddDocumentActionsRequest from a dict
add_document_actions_request_from_dict = AddDocumentActionsRequest.from_dict(add_document_actions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


