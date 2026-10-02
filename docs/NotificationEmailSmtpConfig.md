# NotificationEmailSmtpConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | SMTP server hostname | 
**port** | **int** | SMTP server port | 
**connection_security** | [**NotificationEmailSmtpConnectionSecurity**](NotificationEmailSmtpConnectionSecurity.md) |  | 
**credentials_secret_arn** | **str** | AWS Secrets Manager ARN for a secret whose value is a JSON object containing non-empty string properties named \&quot;username\&quot; and \&quot;password\&quot;, for example: {\&quot;username\&quot;:\&quot;smtp-user@example.com\&quot;,\&quot;password\&quot;:\&quot;smtp-password\&quot;}. | 

## Example

```python
from formkiq_client.models.notification_email_smtp_config import NotificationEmailSmtpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEmailSmtpConfig from a JSON string
notification_email_smtp_config_instance = NotificationEmailSmtpConfig.from_json(json)
# print the JSON string representation of the object
print(NotificationEmailSmtpConfig.to_json())

# convert the object into a dict
notification_email_smtp_config_dict = notification_email_smtp_config_instance.to_dict()
# create an instance of NotificationEmailSmtpConfig from a dict
notification_email_smtp_config_from_dict = NotificationEmailSmtpConfig.from_dict(notification_email_smtp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


