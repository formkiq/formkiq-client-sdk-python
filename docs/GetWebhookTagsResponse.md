# GetWebhookTagsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**previous** | **str** | Previous page of results token | [optional] 
**tags** | [**List[WebhookTag]**](WebhookTag.md) | List of webhook tags | [optional] 

## Example

```python
from formkiq_client.models.get_webhook_tags_response import GetWebhookTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhookTagsResponse from a JSON string
get_webhook_tags_response_instance = GetWebhookTagsResponse.from_json(json)
# print the JSON string representation of the object
print(GetWebhookTagsResponse.to_json())

# convert the object into a dict
get_webhook_tags_response_dict = get_webhook_tags_response_instance.to_dict()
# create an instance of GetWebhookTagsResponse from a dict
get_webhook_tags_response_from_dict = GetWebhookTagsResponse.from_dict(get_webhook_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


