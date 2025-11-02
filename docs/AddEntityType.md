# AddEntityType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | [**EntityTypeNamespace**](EntityTypeNamespace.md) |  | [optional] 
**name** | **str** | Entity Type Name | [optional] 

## Example

```python
from openapi_client.model.add_entity_type import AddEntityType

# TODO update the JSON string below
json = "{}"
# create an instance of AddEntityType from a JSON string
add_entity_type_instance = AddEntityType.from_json(json)
# print the JSON string representation of the object
print(AddEntityType.to_json())

# convert the object into a dict
add_entity_type_dict = add_entity_type_instance.to_dict()
# create an instance of AddEntityType from a dict
add_entity_type_from_dict = AddEntityType.from_dict(add_entity_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


