# DocumentSearchTags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **str** | Searches for strings that eq | [optional] 
**begins_with** | **str** | Searches for strings that begin with | [optional] 
**range** | [**DocumentSearchRange**](DocumentSearchRange.md) |  | [optional] 
**key** | **str** | Tag key to search | 

## Example

```python
from formkiq_client.models.document_search_tags import DocumentSearchTags

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchTags from a JSON string
document_search_tags_instance = DocumentSearchTags.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchTags.to_json())

# convert the object into a dict
document_search_tags_dict = document_search_tags_instance.to_dict()
# create an instance of DocumentSearchTags from a dict
document_search_tags_from_dict = DocumentSearchTags.from_dict(document_search_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


