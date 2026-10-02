# AddDocumentNotificationRequest

At least one CC or BCC recipient is required

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_type** | [**DocumentNotificationType**](DocumentNotificationType.md) |  | 
**cc** | **List[str]** | CC recipient email addresses | [optional] 
**bcc** | **List[str]** | BCC recipient email addresses | [optional] 
**subject** | **str** | Notification subject | 
**body** | **str** | Notification body | 

## Example

```python
from formkiq_client.models.add_document_notification_request import AddDocumentNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentNotificationRequest from a JSON string
add_document_notification_request_instance = AddDocumentNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentNotificationRequest.to_json())

# convert the object into a dict
add_document_notification_request_dict = add_document_notification_request_instance.to_dict()
# create an instance of AddDocumentNotificationRequest from a dict
add_document_notification_request_from_dict = AddDocumentNotificationRequest.from_dict(add_document_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


