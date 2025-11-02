# DocumentAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**DocumentActionStatus**](DocumentActionStatus.md) |  | [optional] 
**type** | [**DocumentActionType**](DocumentActionType.md) |  | [optional] 
**retry_count** | **float** | The number of times this action has already been attempted | [optional] 
**max_retries** | **float** | The maximum number of retry attempts allowed for this action | [optional] 
**queue_id** | **str** | Queue Id | [optional] 
**workflow_id** | **str** | Workflow Id | [optional] 
**workflow_step_id** | **str** | Workflow Step Id | [optional] 
**message** | **str** | Action message information | [optional] 
**user_id** | **str** | User who requested the Action | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**start_date** | **str** | Started Timestamp | [optional] 
**completed_date** | **str** | Completed Timestamp | [optional] 
**parameters** | **Dict[str, object]** | Action parameters | [optional] 
**metadata** | **Dict[str, str]** | Action metadata | [optional] 

## Example

```python
from openapi_client.model.document_action import DocumentAction

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAction from a JSON string
document_action_instance = DocumentAction.from_json(json)
# print the JSON string representation of the object
print(DocumentAction.to_json())

# convert the object into a dict
document_action_dict = document_action_instance.to_dict()
# create an instance of DocumentAction from a dict
document_action_from_dict = DocumentAction.from_dict(document_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


