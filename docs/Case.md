# Case


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_id** | **str** | Case Identifier | [optional] 
**case_number** | **str** | Case Number | [optional] 
**document_number** | **str** | Document Number | [optional] 
**planned_start_date** | **str** | Planned Start Date | [optional] 
**start_date** | **str** | Start Date | [optional] 
**end_date** | **str** | End Date | [optional] 
**due_date** | **str** | Due Date | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**name** | **str** | Case Name | [optional] 
**description** | **str** | Case Description | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**status** | [**CaseStatus**](CaseStatus.md) |  | [optional] 
**user_id** | **str** | User who added document | [optional] 

## Example

```python
from formkiq_client.models.case import Case

# TODO update the JSON string below
json = "{}"
# create an instance of Case from a JSON string
case_instance = Case.from_json(json)
# print the JSON string representation of the object
print(Case.to_json())

# convert the object into a dict
case_dict = case_instance.to_dict()
# create an instance of Case from a dict
case_from_dict = Case.from_dict(case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


