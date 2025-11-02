# UserActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**UserActivityType**](UserActivityType.md) |  | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**user_id** | **str** | User who added document | [optional] 
**document** | [**Document**](Document.md) |  | [optional] 
**changes** | [**Dict[str, UserActivityChanges]**](UserActivityChanges.md) |  | [optional] 

## Example

```python
from openapi_client.model.user_activity import UserActivity

# TODO update the JSON string below
json = "{}"
# create an instance of UserActivity from a JSON string
user_activity_instance = UserActivity.from_json(json)
# print the JSON string representation of the object
print(UserActivity.to_json())

# convert the object into a dict
user_activity_dict = user_activity_instance.to_dict()
# create an instance of UserActivity from a dict
user_activity_from_dict = UserActivity.from_dict(user_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


