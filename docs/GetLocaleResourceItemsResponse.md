# GetLocaleResourceItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**resource_items** | [**List[ResourceItem]**](ResourceItem.md) | List of permissions | [optional] 

## Example

```python
from formkiq_client.models.get_locale_resource_items_response import GetLocaleResourceItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLocaleResourceItemsResponse from a JSON string
get_locale_resource_items_response_instance = GetLocaleResourceItemsResponse.from_json(json)
# print the JSON string representation of the object
print(GetLocaleResourceItemsResponse.to_json())

# convert the object into a dict
get_locale_resource_items_response_dict = get_locale_resource_items_response_instance.to_dict()
# create an instance of GetLocaleResourceItemsResponse from a dict
get_locale_resource_items_response_from_dict = GetLocaleResourceItemsResponse.from_dict(get_locale_resource_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


