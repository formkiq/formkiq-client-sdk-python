# AddAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DocumentActionType**](DocumentActionType.md) |  | 
**parameters** | [**AddActionParameters**](AddActionParameters.md) |  | [optional] 
**queue_id** | **str** | Id of Queue | [optional] 

## Example

```python
from openapi_client.models.add_action import AddAction

# TODO update the JSON string below
json = "{}"
# create an instance of AddAction from a JSON string
add_action_instance = AddAction.from_json(json)
# print the JSON string representation of the object
print(AddAction.to_json())

# convert the object into a dict
add_action_dict = add_action_instance.to_dict()
# create an instance of AddAction from a dict
add_action_from_dict = AddAction.from_dict(add_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


