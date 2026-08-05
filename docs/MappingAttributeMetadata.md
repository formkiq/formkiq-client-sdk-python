# MappingAttributeMetadata

Mapping Attribute from document metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** | Attribute Key | 
**source_type** | [**MappingAttributeSourceType**](MappingAttributeSourceType.md) |  | 
**default_value** | **str** | Default value used when no matching value is found | [optional] 
**default_values** | **List[str]** | Default values used when no matching value is found | [optional] 
**label_texts** | **List[str]** | Label Texts | 
**label_matching_type** | [**MappingAttributeLabelMatchingType**](MappingAttributeLabelMatchingType.md) |  | 
**metadata_field** | [**MappingAttributeMetadataField**](MappingAttributeMetadataField.md) |  | 

## Example

```python
from formkiq_client.models.mapping_attribute_metadata import MappingAttributeMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of MappingAttributeMetadata from a JSON string
mapping_attribute_metadata_instance = MappingAttributeMetadata.from_json(json)
# print the JSON string representation of the object
print(MappingAttributeMetadata.to_json())

# convert the object into a dict
mapping_attribute_metadata_dict = mapping_attribute_metadata_instance.to_dict()
# create an instance of MappingAttributeMetadata from a dict
mapping_attribute_metadata_from_dict = MappingAttributeMetadata.from_dict(mapping_attribute_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


