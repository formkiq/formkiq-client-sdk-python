# AddEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Entity Name | [optional] 
**attributes** | [**List[AddEntityAttribute]**](AddEntityAttribute.md) | List of Entity Attributes | [optional] 

## Example

```python
from formkiq_client.models.add_entity import AddEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AddEntity from a JSON string
add_entity_instance = AddEntity.from_json(json)
# print the JSON string representation of the object
print(AddEntity.to_json())

# convert the object into a dict
add_entity_dict = add_entity_instance.to_dict()
# create an instance of AddEntity from a dict
add_entity_from_dict = AddEntity.from_dict(add_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


