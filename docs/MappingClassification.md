# MappingClassification

Mapping Classification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification_id** | **str** | Classification Identifier | 
**conditions** | [**List[MappingClassificationCondition]**](MappingClassificationCondition.md) | List of classification conditions | [optional] 

## Example

```python
from formkiq_client.models.mapping_classification import MappingClassification

# TODO update the JSON string below
json = "{}"
# create an instance of MappingClassification from a JSON string
mapping_classification_instance = MappingClassification.from_json(json)
# print the JSON string representation of the object
print(MappingClassification.to_json())

# convert the object into a dict
mapping_classification_dict = mapping_classification_instance.to_dict()
# create an instance of MappingClassification from a dict
mapping_classification_from_dict = MappingClassification.from_dict(mapping_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


