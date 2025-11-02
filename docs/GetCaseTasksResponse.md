# GetCaseTasksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**tasks** | [**List[Task]**](Task.md) | List of tasks | [optional] 

## Example

```python
from openapi_client.models.get_case_tasks_response import GetCaseTasksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCaseTasksResponse from a JSON string
get_case_tasks_response_instance = GetCaseTasksResponse.from_json(json)
# print the JSON string representation of the object
print(GetCaseTasksResponse.to_json())

# convert the object into a dict
get_case_tasks_response_dict = get_case_tasks_response_instance.to_dict()
# create an instance of GetCaseTasksResponse from a dict
get_case_tasks_response_from_dict = GetCaseTasksResponse.from_dict(get_case_tasks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


