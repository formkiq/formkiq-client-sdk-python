# UserActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | Activity identifier | [optional] 
**type** | **str** | The type of the activity | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**user_id** | **str** | User who added document | [optional] 
**version_key** | **str** | Document Version Identifier | [optional] 
**time_to_live** | **str** | User activity time to live | [optional] 

## Example

```python
from formkiq_client.models.user_activity import UserActivity

# TODO update the JSON string below
json = "{}"
# create an instance of UserActivity from a JSON string
user_activity_instance = UserActivity.from_json(json)
# print the JSON string representation of the object
print(UserActivity.to_json())

# convert the object into a dict
user_activity_dict = user_activity_instance.to_dict()
# create an instance of UserActivity from a dict
user_activity_form_dict = user_activity.from_dict(user_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


