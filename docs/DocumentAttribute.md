# DocumentAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Attribute key | [optional] 
**json_value** | **Dict[str, object]** | One JSON object stored as a single attribute value. Arrays, scalars, and null are not accepted at the top level. Nested values may include objects, arrays, strings, numbers, booleans, and null. Empty objects and nested empty arrays are accepted. Object property order and original number formatting are not preserved.  The complete stored DynamoDB item, including metadata and attribute names, must fit within 400 KB. Stored document nesting must not exceed 32 levels, including the wrapper. Numbers must fit within DynamoDB&#39;s supported range and 38 digits of precision. | [optional] 
**string_value** | **str** | Attribute with string value | [optional] 
**string_values** | **List[str]** | Attribute with string values | [optional] 
**number_value** | **float** | Attribute with number value | [optional] 
**number_values** | **List[float]** | Attribute with number values | [optional] 
**boolean_value** | **bool** | Attribute with boolean value | [optional] 
**date_value** | **str** | Attribute with date value | [optional] 
**date_values** | **List[str]** | Attribute with date values | [optional] 
**inserted_date** | **str** | Earliest insertion timestamp across the attribute&#39;s current values. Adding a value preserves this timestamp; removing values recomputes it from the remaining values. May be absent for older records. | [optional] [readonly] 
**last_modified_date** | **str** | Latest modification timestamp across the attribute&#39;s current values. Removing values recomputes this timestamp from the remaining values; it does not track the time of removal. For older values without a modification timestamp, their insertion timestamp is used when available. May be absent when no timestamp is available. | [optional] [readonly] 
**user_id** | **str** | User who added attribute | [optional] 
**value_type** | [**AttributeValueType**](AttributeValueType.md) |  | [optional] 
**entity** | [**Entity**](Entity.md) |  | [optional] 
**entities** | [**List[Entity]**](Entity.md) | Attribute with entity values | [optional] 

## Example

```python
from formkiq_client.models.document_attribute import DocumentAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAttribute from a JSON string
document_attribute_instance = DocumentAttribute.from_json(json)
# print the JSON string representation of the object
print(DocumentAttribute.to_json())

# convert the object into a dict
document_attribute_dict = document_attribute_instance.to_dict()
# create an instance of DocumentAttribute from a dict
document_attribute_from_dict = DocumentAttribute.from_dict(document_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


