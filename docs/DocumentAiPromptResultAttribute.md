# DocumentAiPromptResultAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Document AI prompt result attribute key | 
**string_values** | **List[str]** | Document AI prompt result attribute string values | 

## Example

```python
from formkiq_client.models.document_ai_prompt_result_attribute import DocumentAiPromptResultAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAiPromptResultAttribute from a JSON string
document_ai_prompt_result_attribute_instance = DocumentAiPromptResultAttribute.from_json(json)
# print the JSON string representation of the object
print(DocumentAiPromptResultAttribute.to_json())

# convert the object into a dict
document_ai_prompt_result_attribute_dict = document_ai_prompt_result_attribute_instance.to_dict()
# create an instance of DocumentAiPromptResultAttribute from a dict
document_ai_prompt_result_attribute_from_dict = DocumentAiPromptResultAttribute.from_dict(document_ai_prompt_result_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


