# DocusignNotificationExpirations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expire_after** | **str** | An integer that sets the number of days the envelope is active. For this value to be used, expireEnabled must be explicitly set to true. | [optional] 
**expire_enabled** | **str** | When true, the envelope expires in the number of days set by expireAfter. | [optional] 
**expire_warn** | **str** | An integer that specifying the number of days before the envelope expires that an expiration warning email is sent to the recipient. | [optional] 

## Example

```python
from openapi_client.models.docusign_notification_expirations import DocusignNotificationExpirations

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignNotificationExpirations from a JSON string
docusign_notification_expirations_instance = DocusignNotificationExpirations.from_json(json)
# print the JSON string representation of the object
print(DocusignNotificationExpirations.to_json())

# convert the object into a dict
docusign_notification_expirations_dict = docusign_notification_expirations_instance.to_dict()
# create an instance of DocusignNotificationExpirations from a dict
docusign_notification_expirations_from_dict = DocusignNotificationExpirations.from_dict(docusign_notification_expirations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


