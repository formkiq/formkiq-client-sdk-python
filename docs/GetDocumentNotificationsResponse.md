# GetDocumentNotificationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**notifications** | [**List[DocumentNotification]**](DocumentNotification.md) | List of document notifications | [optional] 

## Example

```python
from formkiq_client.models.get_document_notifications_response import GetDocumentNotificationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentNotificationsResponse from a JSON string
get_document_notifications_response_instance = GetDocumentNotificationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentNotificationsResponse.to_json())

# convert the object into a dict
get_document_notifications_response_dict = get_document_notifications_response_instance.to_dict()
# create an instance of GetDocumentNotificationsResponse from a dict
get_document_notifications_response_from_dict = GetDocumentNotificationsResponse.from_dict(get_document_notifications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


