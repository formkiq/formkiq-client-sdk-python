# AddResourceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | [**LocaleResourceType**](LocaleResourceType.md) |  | 
**localized_value** | **str** | Localized Value | 
**interface_key** | **str** | Interface Key | 
**attribute_key** | **str** | Attribute Key | 
**allowed_value** | **str** | Resource value | 
**classification_id** | **str** | Classification Id | 

## Example

```python
from formkiq_client.models.add_resource_item import AddResourceItem

# TODO update the JSON string below
json = "{}"
# create an instance of AddResourceItem from a JSON string
add_resource_item_instance = AddResourceItem.from_json(json)
# print the JSON string representation of the object
print(AddResourceItem.to_json())

# convert the object into a dict
add_resource_item_dict = add_resource_item_instance.to_dict()
# create an instance of AddResourceItem from a dict
add_resource_item_from_dict = AddResourceItem.from_dict(add_resource_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


