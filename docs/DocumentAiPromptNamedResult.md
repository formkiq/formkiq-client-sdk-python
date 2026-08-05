# DocumentAiPromptNamedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**llm_prompt_entity_name** | **str** | Name of the LLM Prompt Entity | 
**analysis_category** | **str** | Analysis Category | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**content** | **str** | Result content | [optional] 
**user_id** | **str** | UserId that created Result | [optional] 
**values** | [**List[DocumentAiPromptValue]**](DocumentAiPromptValue.md) | Document AI prompt values | [optional] 

## Example

```python
from formkiq_client.models.document_ai_prompt_named_result import DocumentAiPromptNamedResult

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAiPromptNamedResult from a JSON string
document_ai_prompt_named_result_instance = DocumentAiPromptNamedResult.from_json(json)
# print the JSON string representation of the object
print(DocumentAiPromptNamedResult.to_json())

# convert the object into a dict
document_ai_prompt_named_result_dict = document_ai_prompt_named_result_instance.to_dict()
# create an instance of DocumentAiPromptNamedResult from a dict
document_ai_prompt_named_result_from_dict = DocumentAiPromptNamedResult.from_dict(document_ai_prompt_named_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


