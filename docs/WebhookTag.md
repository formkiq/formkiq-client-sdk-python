# WebhookTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**webhook_id** | **str** | Webhook Identifier | [optional] 
**type** | **str** | Tag type | [optional] 
**user_id** | **str** | User who added document | [optional] 
**value** | **str** | Tag value | 
**key** | **str** | Tag key | 

## Example

```python
from openapi_client.model.webhook_tag import WebhookTag

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTag from a JSON string
webhook_tag_instance = WebhookTag.from_json(json)
# print the JSON string representation of the object
print(WebhookTag.to_json())

# convert the object into a dict
webhook_tag_dict = webhook_tag_instance.to_dict()
# create an instance of WebhookTag from a dict
webhook_tag_from_dict = WebhookTag.from_dict(webhook_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


