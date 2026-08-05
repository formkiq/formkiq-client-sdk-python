# DocumentAiPromptValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_type** | [**DocumentAiPromptResultType**](DocumentAiPromptResultType.md) |  | 
**entity_type** | **str** | Entity type when resultType is ENTITY | [optional] 
**entity_namespace** | [**EntityTypeNamespace**](EntityTypeNamespace.md) |  | [optional] 
**attributes** | [**List[DocumentAiPromptResultAttribute]**](DocumentAiPromptResultAttribute.md) | Attributes extracted from result content | 

## Example

```python
from formkiq_client.models.document_ai_prompt_value import DocumentAiPromptValue

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAiPromptValue from a JSON string
document_ai_prompt_value_instance = DocumentAiPromptValue.from_json(json)
# print the JSON string representation of the object
print(DocumentAiPromptValue.to_json())

# convert the object into a dict
document_ai_prompt_value_dict = document_ai_prompt_value_instance.to_dict()
# create an instance of DocumentAiPromptValue from a dict
document_ai_prompt_value_from_dict = DocumentAiPromptValue.from_dict(document_ai_prompt_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


