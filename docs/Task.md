# Task


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Task Identifier | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**name** | **str** | Name of Task | [optional] 
**description** | **str** | Description of Task | [optional] 
**planned_start_date** | **str** | Planned Start Date of Task | [optional] 
**start_date** | **str** | Start Date of Task | [optional] 
**end_date** | **str** | End Date of Task | [optional] 
**due_date** | **str** | Due Date of Task | [optional] 
**user_id** | **str** | User who added Task | [optional] 
**status** | [**TaskStatus**](TaskStatus.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openapi_client.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


