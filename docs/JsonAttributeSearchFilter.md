# JsonAttributeSearchFilter

Compare a nested scalar field of an attribute defined with dataType JSON. A path and at least one field comparison are required. All supplied predicates are combined with AND; eqOr matches any supplied value. eq and eqOr accept strings and match string fields or boolean fields represented by the lowercase strings \"true\" and \"false\". Numeric fields do not match eq or eqOr; use numeric bounds instead. Missing fields, null, and objects do not match. Arrays do not match in /search; /searchFulltext can match scalar elements of arrays. beginsWith applies to string fields and gt/gte/lt/lte apply to numeric fields. The legacy range operator is not supported inside a json filter. /searchFulltext uses native OpenSearch field types and indexing limits as described by DocumentFulltextAttribute, including date detection and numeric precision.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path relative to jsonValue, beginning with $. Use dot notation for identifier-like property names, quoted bracket notation for other property names, and zero-based brackets for array positions. Examples: $.customer.name, $[&#39;customer.name&#39;], and $.lineItems[0].quantity. Quoted names may escape characters using a backslash. At least one property or array position is required. Wildcards, recursive descent, slices, and filter expressions are not supported. For /searchFulltext, only property paths are supported: $.lineItems.sku matches any array element, while $.lineItems[0].sku is rejected. Dotted property names are treated as OpenSearch field paths rather than distinct literal keys. | 
**eq** | **str** | Match a JSON string field or a boolean field using \&quot;true\&quot; or \&quot;false\&quot;. | [optional] 
**eq_or** | **List[str]** | Match a JSON string field or a boolean field against any provided string; use \&quot;true\&quot; or \&quot;false\&quot; for booleans. | [optional] 
**begins_with** | **str** | JSON string field must begin with this value. | [optional] 
**gt** | **float** | JSON numeric field must be greater than this value. | [optional] 
**gte** | **float** | JSON numeric field must be greater than or equal to this value. | [optional] 
**lt** | **float** | JSON numeric field must be less than this value. | [optional] 
**lte** | **float** | JSON numeric field must be less than or equal to this value. | [optional] 

## Example

```python
from formkiq_client.models.json_attribute_search_filter import JsonAttributeSearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of JsonAttributeSearchFilter from a JSON string
json_attribute_search_filter_instance = JsonAttributeSearchFilter.from_json(json)
# print the JSON string representation of the object
print(JsonAttributeSearchFilter.to_json())

# convert the object into a dict
json_attribute_search_filter_dict = json_attribute_search_filter_instance.to_dict()
# create an instance of JsonAttributeSearchFilter from a dict
json_attribute_search_filter_from_dict = JsonAttributeSearchFilter.from_dict(json_attribute_search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


