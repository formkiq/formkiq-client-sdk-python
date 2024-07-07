# DocumentSearchMatchAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Tag key | [optional] 
**string_value** | **str** | Attribute with string value | [optional] 
**number_value** | **float** | Attribute with number value | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 

## Example

```python
from formkiq_client.models.document_search_match_attribute import DocumentSearchMatchAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchMatchAttribute from a JSON string
document_search_match_attribute_instance = DocumentSearchMatchAttribute.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchMatchAttribute.to_json())

# convert the object into a dict
document_search_match_attribute_dict = document_search_match_attribute_instance.to_dict()
# create an instance of DocumentSearchMatchAttribute from a dict
document_search_match_attribute_from_dict = DocumentSearchMatchAttribute.from_dict(document_search_match_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


