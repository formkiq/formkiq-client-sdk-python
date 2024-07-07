# Nigo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nigo_id** | **str** | Nigo Identifier | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**name** | **str** | Name of Nigo | [optional] 
**description** | **str** | Description of Nigo | [optional] 
**start_date** | **str** | Start Date | [optional] 
**end_date** | **str** | End Date | [optional] 
**user_id** | **str** | User who added Nigo | [optional] 
**status** | [**NigoStatus**](NigoStatus.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from formkiq_client.models.nigo import Nigo

# TODO update the JSON string below
json = "{}"
# create an instance of Nigo from a JSON string
nigo_instance = Nigo.from_json(json)
# print the JSON string representation of the object
print(Nigo.to_json())

# convert the object into a dict
nigo_dict = nigo_instance.to_dict()
# create an instance of Nigo from a dict
nigo_from_dict = Nigo.from_dict(nigo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


