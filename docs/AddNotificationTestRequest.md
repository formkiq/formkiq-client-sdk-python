# AddNotificationTestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | Recipient of the test email | 

## Example

```python
from formkiq_client.models.add_notification_test_request import AddNotificationTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddNotificationTestRequest from a JSON string
add_notification_test_request_instance = AddNotificationTestRequest.from_json(json)
# print the JSON string representation of the object
print(AddNotificationTestRequest.to_json())

# convert the object into a dict
add_notification_test_request_dict = add_notification_test_request_instance.to_dict()
# create an instance of AddNotificationTestRequest from a dict
add_notification_test_request_from_dict = AddNotificationTestRequest.from_dict(add_notification_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


