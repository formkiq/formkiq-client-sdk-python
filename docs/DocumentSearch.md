# DocumentSearch

Document tag search criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Full text search | [optional] 
**meta** | [**DocumentSearchMeta**](DocumentSearchMeta.md) |  | [optional] 
**attribute** | [**DocumentSearchAttribute**](DocumentSearchAttribute.md) |  | [optional] 
**attributes** | [**List[DocumentSearchAttribute]**](DocumentSearchAttribute.md) | List of Composite Key attributes to filter search results on | [optional] 
**tag** | [**DocumentSearchTag**](DocumentSearchTag.md) |  | [optional] 
**tags** | [**List[DocumentSearchTags]**](DocumentSearchTags.md) | List of Composite Key tags to filter search results on | [optional] 
**document_ids** | **List[str]** | List of DocumentIds to filter search results on | [optional] 

## Example

```python
from openapi_client.model.document_search import DocumentSearch

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearch from a JSON string
document_search_instance = DocumentSearch.from_json(json)
# print the JSON string representation of the object
print(DocumentSearch.to_json())

# convert the object into a dict
document_search_dict = document_search_instance.to_dict()
# create an instance of DocumentSearch from a dict
document_search_from_dict = DocumentSearch.from_dict(document_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


