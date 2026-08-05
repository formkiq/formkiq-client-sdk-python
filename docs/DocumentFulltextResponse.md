# DocumentFulltextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | Total number of documents that matched the search query. When the number of matches exceeds 10,000, this value will be reported as 10,000+ unless the search request explicitly enables exact total hit tracking.  | [optional] 
**documents** | [**List[FulltextSearchItem]**](FulltextSearchItem.md) | List of search result documents | [optional] 

## Example

```python
from formkiq_client.models.document_fulltext_response import DocumentFulltextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFulltextResponse from a JSON string
document_fulltext_response_instance = DocumentFulltextResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentFulltextResponse.to_json())

# convert the object into a dict
document_fulltext_response_dict = document_fulltext_response_instance.to_dict()
# create an instance of DocumentFulltextResponse from a dict
document_fulltext_response_from_dict = DocumentFulltextResponse.from_dict(document_fulltext_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


