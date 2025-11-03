# FulltextAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_values** | **List[str]** | Attribute with string values | [optional] 
**number_values** | **List[float]** | Attribute with number values | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 
**value_type** | [**AttributeValueType**](AttributeValueType.md) |  | [optional] 

## Example

```python
from formkiq_client.models.fulltext_attribute import FulltextAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of FulltextAttribute from a JSON string
fulltext_attribute_instance = FulltextAttribute.from_json(json)
# print the JSON string representation of the object
print(FulltextAttribute.to_json())

# convert the object into a dict
fulltext_attribute_dict = fulltext_attribute_instance.to_dict()
# create an instance of FulltextAttribute from a dict
fulltext_attribute_from_dict = FulltextAttribute.from_dict(fulltext_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


