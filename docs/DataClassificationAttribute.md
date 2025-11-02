# DataClassificationAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Data Classification Attribute Key | [optional] 
**value** | **str** | Data Classification Attribute Value | [optional] 

## Example

```python
from openapi_client.models.data_classification_attribute import DataClassificationAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of DataClassificationAttribute from a JSON string
data_classification_attribute_instance = DataClassificationAttribute.from_json(json)
# print the JSON string representation of the object
print(DataClassificationAttribute.to_json())

# convert the object into a dict
data_classification_attribute_dict = data_classification_attribute_instance.to_dict()
# create an instance of DataClassificationAttribute from a dict
data_classification_attribute_from_dict = DataClassificationAttribute.from_dict(data_classification_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


