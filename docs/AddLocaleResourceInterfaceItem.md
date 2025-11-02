# AddLocaleResourceInterfaceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | [**LocaleResourceType**](LocaleResourceType.md) |  | 
**localized_value** | **str** | Localized Value | 
**interface_key** | **str** | Interface Key | 

## Example

```python
from openapi_client.model.add_locale_resource_interface_item import AddLocaleResourceInterfaceItem

# TODO update the JSON string below
json = "{}"
# create an instance of AddLocaleResourceInterfaceItem from a JSON string
add_locale_resource_interface_item_instance = AddLocaleResourceInterfaceItem.from_json(json)
# print the JSON string representation of the object
print(AddLocaleResourceInterfaceItem.to_json())

# convert the object into a dict
add_locale_resource_interface_item_dict = add_locale_resource_interface_item_instance.to_dict()
# create an instance of AddLocaleResourceInterfaceItem from a dict
add_locale_resource_interface_item_from_dict = AddLocaleResourceInterfaceItem.from_dict(add_locale_resource_interface_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


