# SetLocaleResourceItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_item** | [**AddResourceItem**](AddResourceItem.md) |  | [optional] 

## Example

```python
from formkiq_client.models.set_locale_resource_item_request import SetLocaleResourceItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetLocaleResourceItemRequest from a JSON string
set_locale_resource_item_request_instance = SetLocaleResourceItemRequest.from_json(json)
# print the JSON string representation of the object
print(SetLocaleResourceItemRequest.to_json())

# convert the object into a dict
set_locale_resource_item_request_dict = set_locale_resource_item_request_instance.to_dict()
# create an instance of SetLocaleResourceItemRequest from a dict
set_locale_resource_item_request_from_dict = SetLocaleResourceItemRequest.from_dict(set_locale_resource_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


