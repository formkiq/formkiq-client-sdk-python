# GetCaseTaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task** | [**Task**](Task.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_case_task_response import GetCaseTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCaseTaskResponse from a JSON string
get_case_task_response_instance = GetCaseTaskResponse.from_json(json)
# print the JSON string representation of the object
print(GetCaseTaskResponse.to_json())

# convert the object into a dict
get_case_task_response_dict = get_case_task_response_instance.to_dict()
# create an instance of GetCaseTaskResponse from a dict
get_case_task_response_form_dict = get_case_task_response.from_dict(get_case_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


