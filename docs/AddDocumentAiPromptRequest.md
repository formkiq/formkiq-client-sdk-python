# AddDocumentAiPromptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** | Override the LLM Prompt Entity model id | [optional] 

## Example

```python
from formkiq_client.models.add_document_ai_prompt_request import AddDocumentAiPromptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentAiPromptRequest from a JSON string
add_document_ai_prompt_request_instance = AddDocumentAiPromptRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentAiPromptRequest.to_json())

# convert the object into a dict
add_document_ai_prompt_request_dict = add_document_ai_prompt_request_instance.to_dict()
# create an instance of AddDocumentAiPromptRequest from a dict
add_document_ai_prompt_request_from_dict = AddDocumentAiPromptRequest.from_dict(add_document_ai_prompt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


