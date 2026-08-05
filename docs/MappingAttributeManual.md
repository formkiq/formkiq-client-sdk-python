# MappingAttributeManual

Mapping Attribute with manually configured default values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** | Attribute Key | 
**source_type** | [**MappingAttributeSourceType**](MappingAttributeSourceType.md) |  | 
**default_value** | **str** | Default value | [optional] 
**default_values** | **List[str]** | Default values | [optional] 

## Example

```python
from formkiq_client.models.mapping_attribute_manual import MappingAttributeManual

# TODO update the JSON string below
json = "{}"
# create an instance of MappingAttributeManual from a JSON string
mapping_attribute_manual_instance = MappingAttributeManual.from_json(json)
# print the JSON string representation of the object
print(MappingAttributeManual.to_json())

# convert the object into a dict
mapping_attribute_manual_dict = mapping_attribute_manual_instance.to_dict()
# create an instance of MappingAttributeManual from a dict
mapping_attribute_manual_from_dict = MappingAttributeManual.from_dict(mapping_attribute_manual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


