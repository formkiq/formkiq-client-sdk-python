# DocumentNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type_id** | **str** | Reminder Policy entity type identifier | [optional] 
**entity_id** | **str** | Reminder Policy entity identifier | [optional] 
**cc** | **List[str]** | Normalized CC recipient email addresses | [optional] 
**bcc** | **List[str]** | Normalized BCC recipient email addresses | [optional] 
**notification_type** | [**DocumentNotificationType**](DocumentNotificationType.md) |  | [optional] 
**notification_date** | **str** | Scheduled notification occurrence date | [optional] 
**status** | [**DocumentNotificationStatus**](DocumentNotificationStatus.md) |  | [optional] 
**action** | [**DocumentAction**](DocumentAction.md) |  | [optional] 
**inserted_date** | **str** | Inserted timestamp | [optional] 

## Example

```python
from formkiq_client.models.document_notification import DocumentNotification

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentNotification from a JSON string
document_notification_instance = DocumentNotification.from_json(json)
# print the JSON string representation of the object
print(DocumentNotification.to_json())

# convert the object into a dict
document_notification_dict = document_notification_instance.to_dict()
# create an instance of DocumentNotification from a dict
document_notification_from_dict = DocumentNotification.from_dict(document_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


