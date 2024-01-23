# GetDocumentVersionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**documents** | [**List[DocumentVersion]**](DocumentVersion.md) | List of document versions | [optional] 

## Example

```python
from formkiq_client.models.get_document_versions_response import GetDocumentVersionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentVersionsResponse from a JSON string
get_document_versions_response_instance = GetDocumentVersionsResponse.from_json(json)
# print the JSON string representation of the object
print GetDocumentVersionsResponse.to_json()

# convert the object into a dict
get_document_versions_response_dict = get_document_versions_response_instance.to_dict()
# create an instance of GetDocumentVersionsResponse from a dict
get_document_versions_response_form_dict = get_document_versions_response.from_dict(get_document_versions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


