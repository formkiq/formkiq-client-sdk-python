# AddLocaleResourceClassificationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | [**LocaleResourceType**](LocaleResourceType.md) |  | 
**classification_id** | **str** | Classification Id | 
**attribute_key** | **str** | Attribute Key | 
**allowed_value** | **str** | Resource value | 
**localized_value** | **str** | Localized Value | 

## Example

```python
from openapi_client.model.add_locale_resource_classification_item import AddLocaleResourceClassificationItem

# TODO update the JSON string below
json = "{}"
# create an instance of AddLocaleResourceClassificationItem from a JSON string
add_locale_resource_classification_item_instance = AddLocaleResourceClassificationItem.from_json(json)
# print the JSON string representation of the object
print(AddLocaleResourceClassificationItem.to_json())

# convert the object into a dict
add_locale_resource_classification_item_dict = add_locale_resource_classification_item_instance.to_dict()
# create an instance of AddLocaleResourceClassificationItem from a dict
add_locale_resource_classification_item_from_dict = AddLocaleResourceClassificationItem.from_dict(add_locale_resource_classification_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


