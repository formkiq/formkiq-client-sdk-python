# AddNigo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Nigo | 
**description** | **str** | Description of Nigo | [optional] 
**status** | [**NigoStatus**](NigoStatus.md) |  | [optional] 
**planned_start_date** | **str** | Planned Start Date | [optional] 
**start_date** | **str** | Start Date | [optional] 
**end_date** | **str** | End Date | [optional] 
**due_date** | **str** | Due Date | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**document_ids** | **List[str]** |  | [optional] 

## Example

```python
from formkiq_client.models.add_nigo import AddNigo

# TODO update the JSON string below
json = "{}"
# create an instance of AddNigo from a JSON string
add_nigo_instance = AddNigo.from_json(json)
# print the JSON string representation of the object
print(AddNigo.to_json())

# convert the object into a dict
add_nigo_dict = add_nigo_instance.to_dict()
# create an instance of AddNigo from a dict
add_nigo_from_dict = AddNigo.from_dict(add_nigo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


