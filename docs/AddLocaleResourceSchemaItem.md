# AddLocaleResourceSchemaItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | [**LocaleResourceType**](LocaleResourceType.md) |  | 
**attribute_key** | **str** | Attribute Key | 
**allowed_value** | **str** | Resource value | 
**localized_value** | **str** | Localized Value | 

## Example

```python
from openapi_client.models.add_locale_resource_schema_item import AddLocaleResourceSchemaItem

# TODO update the JSON string below
json = "{}"
# create an instance of AddLocaleResourceSchemaItem from a JSON string
add_locale_resource_schema_item_instance = AddLocaleResourceSchemaItem.from_json(json)
# print the JSON string representation of the object
print(AddLocaleResourceSchemaItem.to_json())

# convert the object into a dict
add_locale_resource_schema_item_dict = add_locale_resource_schema_item_instance.to_dict()
# create an instance of AddLocaleResourceSchemaItem from a dict
add_locale_resource_schema_item_from_dict = AddLocaleResourceSchemaItem.from_dict(add_locale_resource_schema_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


