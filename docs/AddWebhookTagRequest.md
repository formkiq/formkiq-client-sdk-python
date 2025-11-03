# AddWebhookTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Tag value | [optional] 
**values** | **List[str]** | Tag values | [optional] 
**key** | **str** | Tag key | [optional] 

## Example

```python
from formkiq_client.models.add_webhook_tag_request import AddWebhookTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddWebhookTagRequest from a JSON string
add_webhook_tag_request_instance = AddWebhookTagRequest.from_json(json)
# print the JSON string representation of the object
print(AddWebhookTagRequest.to_json())

# convert the object into a dict
add_webhook_tag_request_dict = add_webhook_tag_request_instance.to_dict()
# create an instance of AddWebhookTagRequest from a dict
add_webhook_tag_request_from_dict = AddWebhookTagRequest.from_dict(add_webhook_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


