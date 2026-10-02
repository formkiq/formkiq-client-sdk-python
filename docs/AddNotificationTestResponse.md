# AddNotificationTestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Queueing result | 

## Example

```python
from formkiq_client.models.add_notification_test_response import AddNotificationTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddNotificationTestResponse from a JSON string
add_notification_test_response_instance = AddNotificationTestResponse.from_json(json)
# print the JSON string representation of the object
print(AddNotificationTestResponse.to_json())

# convert the object into a dict
add_notification_test_response_dict = add_notification_test_response_instance.to_dict()
# create an instance of AddNotificationTestResponse from a dict
add_notification_test_response_from_dict = AddNotificationTestResponse.from_dict(add_notification_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


