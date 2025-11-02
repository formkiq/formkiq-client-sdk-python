# AddTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Task | [optional] 
**description** | **str** | Description of Task | 
**status** | [**TaskStatus**](TaskStatus.md) |  | [optional] 
**planned_start_date** | **str** | Planned Start Date | [optional] 
**start_date** | **str** | Start Date | [optional] 
**end_date** | **str** | End Date | [optional] 
**due_date** | **str** | Due Date | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**document_ids** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.add_task import AddTask

# TODO update the JSON string below
json = "{}"
# create an instance of AddTask from a JSON string
add_task_instance = AddTask.from_json(json)
# print the JSON string representation of the object
print(AddTask.to_json())

# convert the object into a dict
add_task_dict = add_task_instance.to_dict()
# create an instance of AddTask from a dict
add_task_from_dict = AddTask.from_dict(add_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


