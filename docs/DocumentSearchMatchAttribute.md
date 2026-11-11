# DocumentSearchMatchAttribute

Attribute that supplied the match. For JSON attributes, jsonValue contains the entire stored object, and jsonPath identifies the nested field used by the driving criterion when a path was supplied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Attribute key | [optional] 
**json_value** | **Dict[str, object]** | One JSON object stored as a single attribute value. Arrays, scalars, and null are not accepted at the top level. Nested values may include objects, arrays, strings, numbers, booleans, and null. Empty objects and nested empty arrays are accepted. Object property order and original number formatting are not preserved.  The complete stored DynamoDB item, including metadata and attribute names, must fit within 400 KB. Stored document nesting must not exceed 32 levels, including the wrapper. Numbers must fit within DynamoDB&#39;s supported range and 38 digits of precision. | [optional] 
**json_path** | **str** | Path relative to jsonValue, beginning with $. Use dot notation for identifier-like property names, quoted bracket notation for other property names, and zero-based brackets for array positions. Examples: $.customer.name, $[&#39;customer.name&#39;], and $.lineItems[0].quantity. Quoted names may escape characters using a backslash. At least one property or array position is required. Wildcards, recursive descent, slices, and filter expressions are not supported. For /searchFulltext, only property paths are supported: $.lineItems.sku matches any array element, while $.lineItems[0].sku is rejected. Dotted property names are treated as OpenSearch field paths rather than distinct literal keys. | [optional] 
**string_value** | **str** | Attribute with string value | [optional] 
**number_value** | **float** | Attribute with number value | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 
**date_value** | **str** | Attribute with date value | [optional] 

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


