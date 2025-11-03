# DocumentSearchAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **str** | Searches for strings that eq | [optional] 
**eq_or** | **List[str]** | Searches for ANY strings that eq | [optional] 
**begins_with** | **str** | Searches for strings that begin with | [optional] 
**range** | [**DocumentSearchRange**](DocumentSearchRange.md) |  | [optional] 
**key** | **str** | Attribute key to search | 

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


