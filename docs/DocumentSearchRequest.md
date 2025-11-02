# DocumentSearchRequest

Document search tag criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**DocumentSearch**](DocumentSearch.md) |  | 
**response_fields** | [**SearchResponseFields**](SearchResponseFields.md) |  | [optional] 

## Example

```python
from openapi_client.model.document_search_request import DocumentSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchRequest from a JSON string
document_search_request_instance = DocumentSearchRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchRequest.to_json())

# convert the object into a dict
document_search_request_dict = document_search_request_instance.to_dict()
# create an instance of DocumentSearchRequest from a dict
document_search_request_from_dict = DocumentSearchRequest.from_dict(document_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


