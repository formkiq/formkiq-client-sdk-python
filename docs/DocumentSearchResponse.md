# DocumentSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**previous** | **str** | Previous page of results token | [optional] 
**documents** | [**List[SearchResultDocument]**](SearchResultDocument.md) | List of search result documents | [optional] 

## Example

```python
from openapi_client.model.document_search_response import DocumentSearchResponse

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


