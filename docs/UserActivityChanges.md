# UserActivityChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_value** | **object** | Previous key value | [optional] 
**new_value** | **object** | New key value | [optional] 

## Example

```python
from formkiq_client.models.user_activity_changes import UserActivityChanges

# TODO update the JSON string below
json = "{}"
# create an instance of UserActivityChanges from a JSON string
user_activity_changes_instance = UserActivityChanges.from_json(json)
# print the JSON string representation of the object
print(UserActivityChanges.to_json())

# convert the object into a dict
user_activity_changes_dict = user_activity_changes_instance.to_dict()
# create an instance of UserActivityChanges from a dict
user_activity_changes_from_dict = UserActivityChanges.from_dict(user_activity_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


