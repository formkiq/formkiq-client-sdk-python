# DocumentFulltextAttribute

Full-text attribute search criteria. Use eq or eqOr for scalar attributes and json for nested fields of JSON attributes. json cannot be combined with eq or eqOr. To compare multiple paths in one JSON attribute, use separate criteria with the same key. JSON searches use native OpenSearch indexes. Property paths through arrays match any element; array positions are not supported, and criteria may match different elements. Dotted property names use OpenSearch field-path semantics. Field types are inferred from stored values and must remain compatible across documents. Date-like strings may be indexed as dates, and numeric comparisons use the inferred numeric precision. Exact string and prefix searches use keyword fields; the default dynamic mapping does not index strings longer than 256 characters in keyword fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | [**DocumentFulltextAttributeEq**](DocumentFulltextAttributeEq.md) |  | [optional] 
**eq_or** | [**List[DocumentFulltextAttributeEq]**](DocumentFulltextAttributeEq.md) | Searches for any of the supplied typed attribute values | [optional] 
**var_json** | [**JsonAttributeSearchFilter**](JsonAttributeSearchFilter.md) |  | [optional] 
**key** | **str** | Attribute key to search | 

## Example

```python
from formkiq_client.models.document_fulltext_attribute import DocumentFulltextAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFulltextAttribute from a JSON string
document_fulltext_attribute_instance = DocumentFulltextAttribute.from_json(json)
# print the JSON string representation of the object
print(DocumentFulltextAttribute.to_json())

# convert the object into a dict
document_fulltext_attribute_dict = document_fulltext_attribute_instance.to_dict()
# create an instance of DocumentFulltextAttribute from a dict
document_fulltext_attribute_from_dict = DocumentFulltextAttribute.from_dict(document_fulltext_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


