# SetDocumentDataClassificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**llm_prompt_entity_name** | **str** | Name of the LLM Prompt Entity | 

## Example

```python
from openapi_client.models.set_document_data_classification_request import SetDocumentDataClassificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDocumentDataClassificationRequest from a JSON string
set_document_data_classification_request_instance = SetDocumentDataClassificationRequest.from_json(json)
# print the JSON string representation of the object
print(SetDocumentDataClassificationRequest.to_json())

# convert the object into a dict
set_document_data_classification_request_dict = set_document_data_classification_request_instance.to_dict()
# create an instance of SetDocumentDataClassificationRequest from a dict
set_document_data_classification_request_from_dict = SetDocumentDataClassificationRequest.from_dict(set_document_data_classification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


