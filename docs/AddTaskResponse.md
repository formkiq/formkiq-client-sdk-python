# AddTaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Task Identifier | [optional] 

## Example

```python
from openapi_client.model.add_task_response import AddTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddTaskResponse from a JSON string
add_task_response_instance = AddTaskResponse.from_json(json)
# print the JSON string representation of the object
print(AddTaskResponse.to_json())

# convert the object into a dict
add_task_response_dict = add_task_response_instance.to_dict()
# create an instance of AddTaskResponse from a dict
add_task_response_from_dict = AddTaskResponse.from_dict(add_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


