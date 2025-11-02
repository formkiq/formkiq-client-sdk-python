# AddGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Group | [optional] 
**description** | **str** | Description of Group | [optional] 

## Example

```python
from openapi_client.model.add_group import AddGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AddGroup from a JSON string
add_group_instance = AddGroup.from_json(json)
# print the JSON string representation of the object
print(AddGroup.to_json())

# convert the object into a dict
add_group_dict = add_group_instance.to_dict()
# create an instance of AddGroup from a dict
add_group_from_dict = AddGroup.from_dict(add_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


