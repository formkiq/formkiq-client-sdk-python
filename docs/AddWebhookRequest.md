# AddWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of webhook | 
**ttl** | **str** | Webhook time to live (expiry) | [optional] 
**enabled** | **str** | Is webhook enabled | [optional] 
**tags** | [**List[AddDocumentTag]**](AddDocumentTag.md) | List of document tags | [optional] 

## Example

```python
from formkiq_client.models.add_webhook_request import AddWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddWebhookRequest from a JSON string
add_webhook_request_instance = AddWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(AddWebhookRequest.to_json())

# convert the object into a dict
add_webhook_request_dict = add_webhook_request_instance.to_dict()
# create an instance of AddWebhookRequest from a dict
add_webhook_request_from_dict = AddWebhookRequest.from_dict(add_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


