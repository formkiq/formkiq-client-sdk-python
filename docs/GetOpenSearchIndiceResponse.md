# GetOpenSearchIndiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | [**List[OpenSearchIndex]**](OpenSearchIndex.md) | OpenSearch Indices | [optional] 

## Example

```python
from formkiq_client.models.get_open_search_indice_response import GetOpenSearchIndiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenSearchIndiceResponse from a JSON string
get_open_search_indice_response_instance = GetOpenSearchIndiceResponse.from_json(json)
# print the JSON string representation of the object
print(GetOpenSearchIndiceResponse.to_json())

# convert the object into a dict
get_open_search_indice_response_dict = get_open_search_indice_response_instance.to_dict()
# create an instance of GetOpenSearchIndiceResponse from a dict
get_open_search_indice_response_from_dict = GetOpenSearchIndiceResponse.from_dict(get_open_search_indice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


