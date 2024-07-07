# AddCase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Case Name | 
**status** | [**CaseStatus**](CaseStatus.md) |  | [optional] 
**start_date** | **str** | Start Date | [optional] 
**end_date** | **str** | End Date | [optional] 
**description** | **str** | Case Description | [optional] 
**document_number_format** | [**List[StringFormat]**](StringFormat.md) | Format of Document Number | [optional] 
**case_number_format** | [**List[StringFormat]**](StringFormat.md) | Format of Case Number | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**document_ids** | **List[str]** |  | [optional] 

## Example

```python
from formkiq_client.models.add_case import AddCase

# TODO update the JSON string below
json = "{}"
# create an instance of AddCase from a JSON string
add_case_instance = AddCase.from_json(json)
# print the JSON string representation of the object
print(AddCase.to_json())

# convert the object into a dict
add_case_dict = add_case_instance.to_dict()
# create an instance of AddCase from a dict
add_case_from_dict = AddCase.from_dict(add_case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


