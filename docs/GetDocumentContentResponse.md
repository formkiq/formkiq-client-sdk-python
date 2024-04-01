# GetDocumentContentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Document content | [optional] 
**content_url** | **str** | URL to retrieve document content | [optional] 
**content_type** | **str** | Document Content-Type | [optional] 
**is_base64** | **bool** | Is the content Base64-encoded? | [optional] 

## Example

```python
from formkiq_client.models.get_document_content_response import GetDocumentContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentContentResponse from a JSON string
get_document_content_response_instance = GetDocumentContentResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentContentResponse.to_json())

# convert the object into a dict
get_document_content_response_dict = get_document_content_response_instance.to_dict()
# create an instance of GetDocumentContentResponse from a dict
get_document_content_response_form_dict = get_document_content_response.from_dict(get_document_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


