# SearchResultDocumentAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_values** | **List[str]** | Attribute with string values | [optional] 
**number_values** | **List[float]** | Attribute with number values | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 
**value_type** | [**AttributeValueType**](AttributeValueType.md) |  | [optional] 

## Example

```python
from formkiq_client.models.search_result_document_attribute import SearchResultDocumentAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultDocumentAttribute from a JSON string
search_result_document_attribute_instance = SearchResultDocumentAttribute.from_json(json)
# print the JSON string representation of the object
print(SearchResultDocumentAttribute.to_json())

# convert the object into a dict
search_result_document_attribute_dict = search_result_document_attribute_instance.to_dict()
# create an instance of SearchResultDocumentAttribute from a dict
search_result_document_attribute_from_dict = SearchResultDocumentAttribute.from_dict(search_result_document_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


