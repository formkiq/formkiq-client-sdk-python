# MappingAttributeMetadataExtractionResult

Mapping Attribute from document metadata extraction results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** | Attribute Key | 
**source_type** | [**MappingAttributeSourceType**](MappingAttributeSourceType.md) |  | 
**llm_prompt_entity_name** | **str** | LLM prompt entity name | 

## Example

```python
from formkiq_client.models.mapping_attribute_metadata_extraction_result import MappingAttributeMetadataExtractionResult

# TODO update the JSON string below
json = "{}"
# create an instance of MappingAttributeMetadataExtractionResult from a JSON string
mapping_attribute_metadata_extraction_result_instance = MappingAttributeMetadataExtractionResult.from_json(json)
# print the JSON string representation of the object
print(MappingAttributeMetadataExtractionResult.to_json())

# convert the object into a dict
mapping_attribute_metadata_extraction_result_dict = mapping_attribute_metadata_extraction_result_instance.to_dict()
# create an instance of MappingAttributeMetadataExtractionResult from a dict
mapping_attribute_metadata_extraction_result_from_dict = MappingAttributeMetadataExtractionResult.from_dict(mapping_attribute_metadata_extraction_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


