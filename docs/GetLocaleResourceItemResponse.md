# GetLocaleResourceItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_item** | [**ResourceItem**](ResourceItem.md) |  | [optional] 

## Example

```python
from openapi_client.model.get_locale_resource_item_response import GetLocaleResourceItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLocaleResourceItemResponse from a JSON string
get_locale_resource_item_response_instance = GetLocaleResourceItemResponse.from_json(json)
# print the JSON string representation of the object
print(GetLocaleResourceItemResponse.to_json())

# convert the object into a dict
get_locale_resource_item_response_dict = get_locale_resource_item_response_instance.to_dict()
# create an instance of GetLocaleResourceItemResponse from a dict
get_locale_resource_item_response_from_dict = GetLocaleResourceItemResponse.from_dict(get_locale_resource_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


