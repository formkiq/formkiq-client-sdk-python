# MappingClassificationCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**MappingClassificationConditionSourceType**](MappingClassificationConditionSourceType.md) |  | 
**matching_type** | [**MappingClassificationConditionMatchingType**](MappingClassificationConditionMatchingType.md) |  | 
**text** | **str** | Text to match against the document content | 
**result_key** | **str** | Result key | 
**result_value** | **str** | Result value | 
**llm_prompt_entity_name** | **str** | LLM prompt entity name | 

## Example

```python
from formkiq_client.models.mapping_classification_condition import MappingClassificationCondition

# TODO update the JSON string below
json = "{}"
# create an instance of MappingClassificationCondition from a JSON string
mapping_classification_condition_instance = MappingClassificationCondition.from_json(json)
# print the JSON string representation of the object
print(MappingClassificationCondition.to_json())

# convert the object into a dict
mapping_classification_condition_dict = mapping_classification_condition_instance.to_dict()
# create an instance of MappingClassificationCondition from a dict
mapping_classification_condition_from_dict = MappingClassificationCondition.from_dict(mapping_classification_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


