# UpdateTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task** | [**UpdateTask**](UpdateTask.md) |  | [optional] 

## Example

```python
from formkiq_client.models.update_task_request import UpdateTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaskRequest from a JSON string
update_task_request_instance = UpdateTaskRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTaskRequest.to_json())

# convert the object into a dict
update_task_request_dict = update_task_request_instance.to_dict()
# create an instance of UpdateTaskRequest from a dict
update_task_request_form_dict = update_task_request.from_dict(update_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


