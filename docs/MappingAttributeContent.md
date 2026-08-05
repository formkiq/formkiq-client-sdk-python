# MappingAttributeContent

Mapping Attribute from document content or content key-value data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** | Attribute Key | 
**source_type** | [**MappingAttributeSourceType**](MappingAttributeSourceType.md) |  | 
**default_value** | **str** | Default value used when no matching value is found | [optional] 
**default_values** | **List[str]** | Default values used when no matching value is found | [optional] 
**label_texts** | **List[str]** | Label Texts | 
**label_matching_type** | [**MappingAttributeLabelMatchingType**](MappingAttributeLabelMatchingType.md) |  | 
**validation_regex** | **str** | Attribute Value Regex Validation | [optional] 

## Example

```python
from formkiq_client.models.mapping_attribute_content import MappingAttributeContent

# TODO update the JSON string below
json = "{}"
# create an instance of MappingAttributeContent from a JSON string
mapping_attribute_content_instance = MappingAttributeContent.from_json(json)
# print the JSON string representation of the object
print(MappingAttributeContent.to_json())

# convert the object into a dict
mapping_attribute_content_dict = mapping_attribute_content_instance.to_dict()
# create an instance of MappingAttributeContent from a dict
mapping_attribute_content_from_dict = MappingAttributeContent.from_dict(mapping_attribute_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


