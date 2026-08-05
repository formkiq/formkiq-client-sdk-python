# MappingAttributeDataClassification

Mapping Attribute from document data classification results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** | Attribute Key | 
**source_type** | [**MappingAttributeSourceType**](MappingAttributeSourceType.md) |  | 

## Example

```python
from formkiq_client.models.mapping_attribute_data_classification import MappingAttributeDataClassification

# TODO update the JSON string below
json = "{}"
# create an instance of MappingAttributeDataClassification from a JSON string
mapping_attribute_data_classification_instance = MappingAttributeDataClassification.from_json(json)
# print the JSON string representation of the object
print(MappingAttributeDataClassification.to_json())

# convert the object into a dict
mapping_attribute_data_classification_dict = mapping_attribute_data_classification_instance.to_dict()
# create an instance of MappingAttributeDataClassification from a dict
mapping_attribute_data_classification_from_dict = MappingAttributeDataClassification.from_dict(mapping_attribute_data_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


