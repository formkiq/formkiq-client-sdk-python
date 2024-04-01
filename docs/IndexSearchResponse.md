# IndexSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**previous** | **str** | Previous page of results token | [optional] 
**values** | [**List[IndexSearch]**](IndexSearch.md) | List of search results | [optional] 

## Example

```python
from formkiq_client.models.index_search_response import IndexSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IndexSearchResponse from a JSON string
index_search_response_instance = IndexSearchResponse.from_json(json)
# print the JSON string representation of the object
print(IndexSearchResponse.to_json())

# convert the object into a dict
index_search_response_dict = index_search_response_instance.to_dict()
# create an instance of IndexSearchResponse from a dict
index_search_response_form_dict = index_search_response.from_dict(index_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


