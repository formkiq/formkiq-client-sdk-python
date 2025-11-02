# GetCaseDocumentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**documents** | [**List[Document]**](Document.md) | List of documents | [optional] 

## Example

```python
from openapi_client.models.get_case_documents_response import GetCaseDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCaseDocumentsResponse from a JSON string
get_case_documents_response_instance = GetCaseDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print(GetCaseDocumentsResponse.to_json())

# convert the object into a dict
get_case_documents_response_dict = get_case_documents_response_instance.to_dict()
# create an instance of GetCaseDocumentsResponse from a dict
get_case_documents_response_from_dict = GetCaseDocumentsResponse.from_dict(get_case_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


