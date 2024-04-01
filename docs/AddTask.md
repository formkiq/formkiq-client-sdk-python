# AddTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of Task | 
**status** | [**TaskStatus**](TaskStatus.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**document_ids** | **List[str]** |  | [optional] 

## Example

```python
from formkiq_client.models.add_task import AddTask

# TODO update the JSON string below
json = "{}"
# create an instance of AddTask from a JSON string
add_task_instance = AddTask.from_json(json)
# print the JSON string representation of the object
print(AddTask.to_json())

# convert the object into a dict
add_task_dict = add_task_instance.to_dict()
# create an instance of AddTask from a dict
add_task_form_dict = add_task.from_dict(add_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


