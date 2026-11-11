# SearchResultDocumentAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_value** | **Dict[str, object]** | One JSON object stored as a single attribute value. Arrays, scalars, and null are not accepted at the top level. Nested values may include objects, arrays, strings, numbers, booleans, and null. Empty objects and nested empty arrays are accepted. Object property order and original number formatting are not preserved.  The complete stored DynamoDB item, including metadata and attribute names, must fit within 400 KB. Stored document nesting must not exceed 32 levels, including the wrapper. Numbers must fit within DynamoDB&#39;s supported range and 38 digits of precision. | [optional] 
**string_values** | **List[str]** | Attribute with string values | [optional] 
**number_values** | **List[float]** | Attribute with number values | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 
**date_values** | **List[str]** | Attribute with date values | [optional] 
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


