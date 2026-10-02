# AddDocumentNotificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Notification queueing result | 

## Example

```python
from formkiq_client.models.add_document_notification_response import AddDocumentNotificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentNotificationResponse from a JSON string
add_document_notification_response_instance = AddDocumentNotificationResponse.from_json(json)
# print the JSON string representation of the object
print(AddDocumentNotificationResponse.to_json())

# convert the object into a dict
add_document_notification_response_dict = add_document_notification_response_instance.to_dict()
# create an instance of AddDocumentNotificationResponse from a dict
add_document_notification_response_from_dict = AddDocumentNotificationResponse.from_dict(add_document_notification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


