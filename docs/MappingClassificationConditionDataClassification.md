# MappingClassificationConditionDataClassification

Mapping Classification Condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**MappingClassificationConditionSourceType**](MappingClassificationConditionSourceType.md) |  | 
**result_key** | **str** | Result key | 
**result_value** | **str** | Result value | 
**matching_type** | [**MappingClassificationConditionMatchingType**](MappingClassificationConditionMatchingType.md) |  | 

## Example

```python
from formkiq_client.models.mapping_classification_condition_data_classification import MappingClassificationConditionDataClassification

# TODO update the JSON string below
json = "{}"
# create an instance of MappingClassificationConditionDataClassification from a JSON string
mapping_classification_condition_data_classification_instance = MappingClassificationConditionDataClassification.from_json(json)
# print the JSON string representation of the object
print(MappingClassificationConditionDataClassification.to_json())

# convert the object into a dict
mapping_classification_condition_data_classification_dict = mapping_classification_condition_data_classification_instance.to_dict()
# create an instance of MappingClassificationConditionDataClassification from a dict
mapping_classification_condition_data_classification_from_dict = MappingClassificationConditionDataClassification.from_dict(mapping_classification_condition_data_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


