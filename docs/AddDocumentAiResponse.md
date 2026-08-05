# AddDocumentAiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_prompt** | **str** | System Prompt | [optional] 
**ai_prompt_result** | [**DocumentAiPromptResult**](DocumentAiPromptResult.md) |  | [optional] 

## Example

```python
from formkiq_client.models.add_document_ai_response import AddDocumentAiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentAiResponse from a JSON string
add_document_ai_response_instance = AddDocumentAiResponse.from_json(json)
# print the JSON string representation of the object
print(AddDocumentAiResponse.to_json())

# convert the object into a dict
add_document_ai_response_dict = add_document_ai_response_instance.to_dict()
# create an instance of AddDocumentAiResponse from a dict
add_document_ai_response_from_dict = AddDocumentAiResponse.from_dict(add_document_ai_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


