# UpdateTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Task | [optional] 
**description** | **str** | Description of Task | [optional] 
**start_date** | **str** | Start Date | [optional] 
**end_date** | **str** | End Date | [optional] 
**status** | [**TaskStatus**](TaskStatus.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**document_ids** | **List[str]** |  | [optional] 

## Example

```python
from formkiq_client.models.update_task import UpdateTask

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTask from a JSON string
update_task_instance = UpdateTask.from_json(json)
# print the JSON string representation of the object
print(UpdateTask.to_json())

# convert the object into a dict
update_task_dict = update_task_instance.to_dict()
# create an instance of UpdateTask from a dict
update_task_form_dict = update_task.from_dict(update_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


