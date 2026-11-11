# DocumentSearch

Document tag search criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Full text search | [optional] 
**meta** | [**DocumentSearchMeta**](DocumentSearchMeta.md) |  | [optional] 
**filename** | [**DocumentSearchFilename**](DocumentSearchFilename.md) |  | [optional] 
**folder** | [**DocumentSearchFolder**](DocumentSearchFolder.md) |  | [optional] 
**attribute** | [**DocumentSearchAttribute**](DocumentSearchAttribute.md) |  | [optional] 
**attributes** | [**List[DocumentSearchAttribute]**](DocumentSearchAttribute.md) | Attributes combined with AND. DynamoDB uses a matching schema composite key when available. For index searches, a composite key covering only some attributes is also preferred: the largest usable composite key supplies the initial matches and the remaining attributes filter them. Otherwise, the first attribute supplies matches and the remaining attributes filter them; put the most selective attribute first. No composite key or reindex is required for this fallback. Each fallback index request examines at most 10,000 candidate attribute records. Multivalued attributes may consume multiple candidate records. Results use the first matching value of the driving attribute as matchedAttribute. All conditions must match the same document or artifact. A short or empty document page can still include a next token; continue until next is absent. COUNT can return fewer than 10,000 matches with truncated&#x3D;true when the record or time budget is reached. Existing composite-key ordering and operator restrictions still apply when a composite key is used. JSON path criteria are identified by key and json.path, so the same key may occur more than once with different paths. JSON path criteria do not implicitly participate in existing scalar composite keys. | [optional] 
**tag** | [**DocumentSearchTag**](DocumentSearchTag.md) |  | [optional] 
**tags** | [**List[DocumentSearchTags]**](DocumentSearchTags.md) | List of Composite Key tags to filter search results on | [optional] 
**document_ids** | **List[str]** | List of up to 100 document IDs to check against the search criteria. When supplied, the &#x60;limit&#x60; query parameter is ignored and all matching documents are returned. Cannot be combined with &#x60;filename&#x60;. | [optional] 

## Example

```python
from formkiq_client.models.document_search import DocumentSearch

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


