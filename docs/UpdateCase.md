# UpdateCase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Case Name | [optional] 
**status** | [**CaseStatus**](CaseStatus.md) |  | [optional] 
**description** | **str** | Case Description | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**planned_start_date** | **str** | Planned Start Date | [optional] 
**start_date** | **str** | Start Date | [optional] 
**end_date** | **str** | End Date | [optional] 
**due_date** | **str** | Due Date | [optional] 
**document_ids** | **List[str]** |  | [optional] 

## Example

```python
from formkiq_client.models.update_case import UpdateCase

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCase from a JSON string
update_case_instance = UpdateCase.from_json(json)
# print the JSON string representation of the object
print(UpdateCase.to_json())

# convert the object into a dict
update_case_dict = update_case_instance.to_dict()
# create an instance of UpdateCase from a dict
update_case_from_dict = UpdateCase.from_dict(update_case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


