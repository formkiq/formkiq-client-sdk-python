# DocumentFulltextSearch

Document full text search criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Result page to return (starting at 1) | [optional] 
**text** | **str** | Full text search | [optional] 
**tags** | [**List[DocumentFulltextTag]**](DocumentFulltextTag.md) | List of search tags | [optional] 

## Example

```python
from formkiq_client.models.document_fulltext_search import DocumentFulltextSearch

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFulltextSearch from a JSON string
document_fulltext_search_instance = DocumentFulltextSearch.from_json(json)
# print the JSON string representation of the object
print DocumentFulltextSearch.to_json()

# convert the object into a dict
document_fulltext_search_dict = document_fulltext_search_instance.to_dict()
# create an instance of DocumentFulltextSearch from a dict
document_fulltext_search_form_dict = document_fulltext_search.from_dict(document_fulltext_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


