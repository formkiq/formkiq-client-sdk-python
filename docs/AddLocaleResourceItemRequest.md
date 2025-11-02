# AddLocaleResourceItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_item** | [**AddResourceItem**](AddResourceItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.add_locale_resource_item_request import AddLocaleResourceItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddLocaleResourceItemRequest from a JSON string
add_locale_resource_item_request_instance = AddLocaleResourceItemRequest.from_json(json)
# print the JSON string representation of the object
print(AddLocaleResourceItemRequest.to_json())

# convert the object into a dict
add_locale_resource_item_request_dict = add_locale_resource_item_request_instance.to_dict()
# create an instance of AddLocaleResourceItemRequest from a dict
add_locale_resource_item_request_from_dict = AddLocaleResourceItemRequest.from_dict(add_locale_resource_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


