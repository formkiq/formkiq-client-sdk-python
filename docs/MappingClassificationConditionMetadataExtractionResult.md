# MappingClassificationConditionMetadataExtractionResult

Mapping Classification Condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**MappingClassificationConditionSourceType**](MappingClassificationConditionSourceType.md) |  | 
**llm_prompt_entity_name** | **str** | LLM prompt entity name | 
**result_key** | **str** | Result key | 
**result_value** | **str** | Result value | 
**matching_type** | [**MappingClassificationConditionMatchingType**](MappingClassificationConditionMatchingType.md) |  | 

## Example

```python
from formkiq_client.models.mapping_classification_condition_metadata_extraction_result import MappingClassificationConditionMetadataExtractionResult

# TODO update the JSON string below
json = "{}"
# create an instance of MappingClassificationConditionMetadataExtractionResult from a JSON string
mapping_classification_condition_metadata_extraction_result_instance = MappingClassificationConditionMetadataExtractionResult.from_json(json)
# print the JSON string representation of the object
print(MappingClassificationConditionMetadataExtractionResult.to_json())

# convert the object into a dict
mapping_classification_condition_metadata_extraction_result_dict = mapping_classification_condition_metadata_extraction_result_instance.to_dict()
# create an instance of MappingClassificationConditionMetadataExtractionResult from a dict
mapping_classification_condition_metadata_extraction_result_from_dict = MappingClassificationConditionMetadataExtractionResult.from_dict(mapping_classification_condition_metadata_extraction_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


