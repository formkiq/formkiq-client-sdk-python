# MappingClassificationConditionContent

Mapping Classification Condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**MappingClassificationConditionSourceType**](MappingClassificationConditionSourceType.md) |  | 
**matching_type** | [**MappingClassificationConditionMatchingType**](MappingClassificationConditionMatchingType.md) |  | 
**text** | **str** | Text to match against the document content | 

## Example

```python
from formkiq_client.models.mapping_classification_condition_content import MappingClassificationConditionContent

# TODO update the JSON string below
json = "{}"
# create an instance of MappingClassificationConditionContent from a JSON string
mapping_classification_condition_content_instance = MappingClassificationConditionContent.from_json(json)
# print the JSON string representation of the object
print(MappingClassificationConditionContent.to_json())

# convert the object into a dict
mapping_classification_condition_content_dict = mapping_classification_condition_content_instance.to_dict()
# create an instance of MappingClassificationConditionContent from a dict
mapping_classification_condition_content_from_dict = MappingClassificationConditionContent.from_dict(mapping_classification_condition_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


