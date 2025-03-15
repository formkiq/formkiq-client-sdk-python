# AddLocaleResourceItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_key** | **str** | Item Key of resource | [optional] 

## Example

```python
from formkiq_client.models.add_locale_resource_item_response import AddLocaleResourceItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddLocaleResourceItemResponse from a JSON string
add_locale_resource_item_response_instance = AddLocaleResourceItemResponse.from_json(json)
# print the JSON string representation of the object
print(AddLocaleResourceItemResponse.to_json())

# convert the object into a dict
add_locale_resource_item_response_dict = add_locale_resource_item_response_instance.to_dict()
# create an instance of AddLocaleResourceItemResponse from a dict
add_locale_resource_item_response_from_dict = AddLocaleResourceItemResponse.from_dict(add_locale_resource_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


