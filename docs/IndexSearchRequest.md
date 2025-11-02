# IndexSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_type** | **str** | The name of the index to search | [optional] 

## Example

```python
from openapi_client.model.index_search_request import IndexSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IndexSearchRequest from a JSON string
index_search_request_instance = IndexSearchRequest.from_json(json)
# print the JSON string representation of the object
print(IndexSearchRequest.to_json())

# convert the object into a dict
index_search_request_dict = index_search_request_instance.to_dict()
# create an instance of IndexSearchRequest from a dict
index_search_request_from_dict = IndexSearchRequest.from_dict(index_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


