# AddNigo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of Task | [optional] 
**status** | [**NigoStatus**](NigoStatus.md) |  | [optional] 
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
add_nigo_form_dict = add_nigo.from_dict(add_nigo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


