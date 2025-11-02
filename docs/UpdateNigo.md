# UpdateNigo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Nigo | [optional] 
**description** | **str** | Description of Nigo | [optional] 
**planned_start_date** | **str** | Planned Start Date | [optional] 
**start_date** | **str** | Start Date | [optional] 
**end_date** | **str** | End Date | [optional] 
**due_date** | **str** | Due Date | [optional] 
**status** | [**NigoStatus**](NigoStatus.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**document_ids** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.update_nigo import UpdateNigo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNigo from a JSON string
update_nigo_instance = UpdateNigo.from_json(json)
# print the JSON string representation of the object
print(UpdateNigo.to_json())

# convert the object into a dict
update_nigo_dict = update_nigo_instance.to_dict()
# create an instance of UpdateNigo from a dict
update_nigo_from_dict = UpdateNigo.from_dict(update_nigo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


