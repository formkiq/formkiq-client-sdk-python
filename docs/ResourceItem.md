# ResourceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | [**LocaleResourceType**](LocaleResourceType.md) |  | [optional] 
**localized_value** | **str** | Localized Value | [optional] 
**interface_key** | **str** | Interface Key | [optional] 
**item_key** | **str** | Item Key | [optional] 
**attribute_key** | **str** | Attribute Key | [optional] 
**allowed_value** | **str** | Resource value | [optional] 
**classification_id** | **str** | Classification Id | [optional] 

## Example

```python
from formkiq_client.models.resource_item import ResourceItem

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceItem from a JSON string
resource_item_instance = ResourceItem.from_json(json)
# print the JSON string representation of the object
print(ResourceItem.to_json())

# convert the object into a dict
resource_item_dict = resource_item_instance.to_dict()
# create an instance of ResourceItem from a dict
resource_item_from_dict = ResourceItem.from_dict(resource_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


