# AddTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task** | [**AddTask**](AddTask.md) |  | 

## Example

```python
from formkiq_client.models.add_task_request import AddTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTaskRequest from a JSON string
add_task_request_instance = AddTaskRequest.from_json(json)
# print the JSON string representation of the object
print(AddTaskRequest.to_json())

# convert the object into a dict
add_task_request_dict = add_task_request_instance.to_dict()
# create an instance of AddTaskRequest from a dict
add_task_request_from_dict = AddTaskRequest.from_dict(add_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


