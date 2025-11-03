# DocusignNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_account_defaults** | **str** | When true, the account default notification settings are used for the envelope, overriding the reminders and expirations settings. When false, the reminders and expirations settings specified in this request are used. The default value is false. | [optional] 
**expirations** | [**DocusignNotificationExpirations**](DocusignNotificationExpirations.md) |  | [optional] 
**reminders** | [**DocusignNotificationReminders**](DocusignNotificationReminders.md) |  | [optional] 

## Example

```python
from formkiq_client.models.docusign_notification import DocusignNotification

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignNotification from a JSON string
docusign_notification_instance = DocusignNotification.from_json(json)
# print the JSON string representation of the object
print(DocusignNotification.to_json())

# convert the object into a dict
docusign_notification_dict = docusign_notification_instance.to_dict()
# create an instance of DocusignNotification from a dict
docusign_notification_from_dict = DocusignNotification.from_dict(docusign_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


