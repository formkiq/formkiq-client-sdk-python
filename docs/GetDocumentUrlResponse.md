# GetDocumentUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document Identifier | [optional] 
**url** | **str** | Document content url | [optional] 
**headers** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openapi_client.model.get_document_url_response import GetDocumentUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentUrlResponse from a JSON string
get_document_url_response_instance = GetDocumentUrlResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentUrlResponse.to_json())

# convert the object into a dict
get_document_url_response_dict = get_document_url_response_instance.to_dict()
# create an instance of GetDocumentUrlResponse from a dict
get_document_url_response_from_dict = GetDocumentUrlResponse.from_dict(get_document_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


