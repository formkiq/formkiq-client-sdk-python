# MappingAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** | Attribute Key | [optional] 
**source_type** | [**MappingAttributeSourceType**](MappingAttributeSourceType.md) |  | [optional] 
**default_value** | **str** | Default value | [optional] 
**default_values** | **List[str]** | Default values | [optional] 
**label_texts** | **List[str]** |  | [optional] 
**label_matching_type** | [**MappingAttributeLabelMatchingType**](MappingAttributeLabelMatchingType.md) |  | [optional] 
**metadata_field** | [**MappingAttributeMetadataField**](MappingAttributeMetadataField.md) |  | [optional] 
**validation_regex** | **str** | Attribute Value Regex Validation | [optional] 

## Example

```python
from openapi_client.model.mapping_attribute import MappingAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of MappingAttribute from a JSON string
mapping_attribute_instance = MappingAttribute.from_json(json)
# print the JSON string representation of the object
print(MappingAttribute.to_json())

# convert the object into a dict
mapping_attribute_dict = mapping_attribute_instance.to_dict()
# create an instance of MappingAttribute from a dict
mapping_attribute_from_dict = MappingAttribute.from_dict(mapping_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


