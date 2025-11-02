# AddWebhookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **str** |  | [optional] 
**site_id** | **str** | Site Identifier | [optional] 

## Example

```python
from openapi_client.model.add_webhook_response import AddWebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddWebhookResponse from a JSON string
add_webhook_response_instance = AddWebhookResponse.from_json(json)
# print the JSON string representation of the object
print(AddWebhookResponse.to_json())

# convert the object into a dict
add_webhook_response_dict = add_webhook_response_instance.to_dict()
# create an instance of AddWebhookResponse from a dict
add_webhook_response_from_dict = AddWebhookResponse.from_dict(add_webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


