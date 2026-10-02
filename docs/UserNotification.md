# UserNotification

A document notification associated with the authenticated user's email address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier | [optional] 
**artifact_id** | **str** | Document artifact identifier | [optional] 
**notification** | [**DocumentNotification**](DocumentNotification.md) |  | [optional] 

## Example

```python
from formkiq_client.models.user_notification import UserNotification

# TODO update the JSON string below
json = "{}"
# create an instance of UserNotification from a JSON string
user_notification_instance = UserNotification.from_json(json)
# print the JSON string representation of the object
print(UserNotification.to_json())

# convert the object into a dict
user_notification_dict = user_notification_instance.to_dict()
# create an instance of UserNotification from a dict
user_notification_from_dict = UserNotification.from_dict(user_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


