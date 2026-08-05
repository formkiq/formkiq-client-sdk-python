# GetDocumentAiPromptResultsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**ai_prompt_results** | [**List[DocumentAiPromptResult]**](DocumentAiPromptResult.md) | List of document AI prompt result records | [optional] 

## Example

```python
from formkiq_client.models.get_document_ai_prompt_results_response import GetDocumentAiPromptResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentAiPromptResultsResponse from a JSON string
get_document_ai_prompt_results_response_instance = GetDocumentAiPromptResultsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentAiPromptResultsResponse.to_json())

# convert the object into a dict
get_document_ai_prompt_results_response_dict = get_document_ai_prompt_results_response_instance.to_dict()
# create an instance of GetDocumentAiPromptResultsResponse from a dict
get_document_ai_prompt_results_response_from_dict = GetDocumentAiPromptResultsResponse.from_dict(get_document_ai_prompt_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


