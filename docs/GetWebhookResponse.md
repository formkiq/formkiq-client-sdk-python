# GetWebhookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **str** | Site Identifier | [optional] 
**name** | **str** | Webhook name | [optional] 
**url** | **str** | Webhook url | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**webhook_id** | **str** | Webhook Identifier | [optional] 
**user_id** | **str** | User who added document | [optional] 
**enabled** | **str** | Is webhook enabled | [optional] 

## Example

```python
from formkiq_client.models.get_webhook_response import GetWebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhookResponse from a JSON string
get_webhook_response_instance = GetWebhookResponse.from_json(json)
# print the JSON string representation of the object
print GetWebhookResponse.to_json()

# convert the object into a dict
get_webhook_response_dict = get_webhook_response_instance.to_dict()
# create an instance of GetWebhookResponse from a dict
get_webhook_response_form_dict = get_webhook_response.from_dict(get_webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


