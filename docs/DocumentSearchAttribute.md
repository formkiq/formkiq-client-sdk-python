# DocumentSearchAttribute

Attribute search criterion. Existing eq and eqOr operators accept strings. To compare a nested field of a JSON attribute, supply a json filter containing the path and comparisons. A json filter cannot be combined with the top-level eq, eqOr, beginsWith, or range operators in the same criterion. Use separate criteria in query.attributes to compare multiple JSON paths.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **str** | Searches for strings that eq | [optional] 
**eq_or** | **List[str]** | Searches for strings equal to any provided value. Pagination is not supported when &#x60;eqOr&#x60; is used, so no &#x60;nextToken&#x60; is returned. The request limit is applied separately to each value.  | [optional] 
**begins_with** | **str** | Searches for strings that begin with | [optional] 
**range** | [**DocumentSearchRange**](DocumentSearchRange.md) |  | [optional] 
**key** | **str** | Attribute key to search | 
**var_json** | [**JsonAttributeSearchFilter**](JsonAttributeSearchFilter.md) |  | [optional] 

## Example

```python
from formkiq_client.models.document_search_attribute import DocumentSearchAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchAttribute from a JSON string
document_search_attribute_instance = DocumentSearchAttribute.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchAttribute.to_json())

# convert the object into a dict
document_search_attribute_dict = document_search_attribute_instance.to_dict()
# create an instance of DocumentSearchAttribute from a dict
document_search_attribute_from_dict = DocumentSearchAttribute.from_dict(document_search_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


