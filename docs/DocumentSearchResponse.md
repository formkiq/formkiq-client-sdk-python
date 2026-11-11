# DocumentSearchResponse

Document search response. The `DOCUMENTS` projection returns `documents`, `next`, `previous`, and `truncated`. The `COUNT` projection returns `count` and `truncated` instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of document results token; omitted for the COUNT projection | [optional] 
**previous** | **str** | Previous page of document results token; omitted for the COUNT projection | [optional] 
**documents** | [**List[SearchResultDocument]**](SearchResultDocument.md) | List of search result documents; omitted for the COUNT projection | [optional] 
**count** | **int** | Number of matching documents counted, up to 10,000; only returned for the COUNT projection | [optional] 
**truncated** | **bool** | For DOCUMENTS, true when the 10,000 attribute-record budget or the multi-attribute fallback time budget stops the request before the requested page size is reached and search work remains. The response contains matches found so far, possibly none, and a next token to continue with a fresh budget. False when the requested page size is reached or the search is exhausted, even if next is present for ordinary pagination. For COUNT, true when counting stops at the result limit or the attribute-record processing budget or multi-attribute fallback time budget before the search is exhausted. A truncated count is a lower bound, not an exact total; COUNT does not return continuation tokens. | [optional] 

## Example

```python
from formkiq_client.models.document_search_response import DocumentSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchResponse from a JSON string
document_search_response_instance = DocumentSearchResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchResponse.to_json())

# convert the object into a dict
document_search_response_dict = document_search_response_instance.to_dict()
# create an instance of DocumentSearchResponse from a dict
document_search_response_from_dict = DocumentSearchResponse.from_dict(document_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


