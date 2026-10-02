# GetUserNotificationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**notifications** | [**List[UserNotification]**](UserNotification.md) | List of notifications where the authenticated user&#39;s email is a CC or BCC recipient | [optional] 

## Example

```python
from formkiq_client.models.get_user_notifications_response import GetUserNotificationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserNotificationsResponse from a JSON string
get_user_notifications_response_instance = GetUserNotificationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserNotificationsResponse.to_json())

# convert the object into a dict
get_user_notifications_response_dict = get_user_notifications_response_instance.to_dict()
# create an instance of GetUserNotificationsResponse from a dict
get_user_notifications_response_from_dict = GetUserNotificationsResponse.from_dict(get_user_notifications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


