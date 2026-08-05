# MappingAttributeAiPromptResult

Mapping Attribute from document AI Prompt result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** | Attribute Key | 
**source_type** | [**MappingAttributeSourceType**](MappingAttributeSourceType.md) |  | 
**llm_prompt_entity_name** | **str** | LLM prompt entity name | 

## Example

```python
from formkiq_client.models.mapping_attribute_ai_prompt_result import MappingAttributeAiPromptResult

# TODO update the JSON string below
json = "{}"
# create an instance of MappingAttributeAiPromptResult from a JSON string
mapping_attribute_ai_prompt_result_instance = MappingAttributeAiPromptResult.from_json(json)
# print the JSON string representation of the object
print(MappingAttributeAiPromptResult.to_json())

# convert the object into a dict
mapping_attribute_ai_prompt_result_dict = mapping_attribute_ai_prompt_result_instance.to_dict()
# create an instance of MappingAttributeAiPromptResult from a dict
mapping_attribute_ai_prompt_result_from_dict = MappingAttributeAiPromptResult.from_dict(mapping_attribute_ai_prompt_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


