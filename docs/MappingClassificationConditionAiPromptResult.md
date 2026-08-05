# MappingClassificationConditionAiPromptResult

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
from formkiq_client.models.mapping_classification_condition_ai_prompt_result import MappingClassificationConditionAiPromptResult

# TODO update the JSON string below
json = "{}"
# create an instance of MappingClassificationConditionAiPromptResult from a JSON string
mapping_classification_condition_ai_prompt_result_instance = MappingClassificationConditionAiPromptResult.from_json(json)
# print the JSON string representation of the object
print(MappingClassificationConditionAiPromptResult.to_json())

# convert the object into a dict
mapping_classification_condition_ai_prompt_result_dict = mapping_classification_condition_ai_prompt_result_instance.to_dict()
# create an instance of MappingClassificationConditionAiPromptResult from a dict
mapping_classification_condition_ai_prompt_result_from_dict = MappingClassificationConditionAiPromptResult.from_dict(mapping_classification_condition_ai_prompt_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


