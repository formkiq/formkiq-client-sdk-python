# DocusignNotificationReminders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reminder_delay** | **str** | An integer specifying the number of days after the recipient receives the envelope that reminder emails are sent to the recipient. | [optional] 
**reminder_enabled** | **str** | When true, reminders are enabled. The default value is false. | [optional] 
**reminder_frequency** | **str** | An integer specifying the interval in days between reminder emails. | [optional] 

## Example

```python
from openapi_client.model.docusign_notification_reminders import DocusignNotificationReminders

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignNotificationReminders from a JSON string
docusign_notification_reminders_instance = DocusignNotificationReminders.from_json(json)
# print the JSON string representation of the object
print(DocusignNotificationReminders.to_json())

# convert the object into a dict
docusign_notification_reminders_dict = docusign_notification_reminders_instance.to_dict()
# create an instance of DocusignNotificationReminders from a dict
docusign_notification_reminders_from_dict = DocusignNotificationReminders.from_dict(docusign_notification_reminders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


