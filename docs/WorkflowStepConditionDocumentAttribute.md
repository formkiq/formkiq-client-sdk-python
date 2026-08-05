# WorkflowStepConditionDocumentAttribute

Uses a document attribute as the source value for a workflow condition criterion.  The attribute is selected using `attributeKey`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** | Document attribute key | 

## Example

```python
from formkiq_client.models.workflow_step_condition_document_attribute import WorkflowStepConditionDocumentAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepConditionDocumentAttribute from a JSON string
workflow_step_condition_document_attribute_instance = WorkflowStepConditionDocumentAttribute.from_json(json)
# print the JSON string representation of the object
print(WorkflowStepConditionDocumentAttribute.to_json())

# convert the object into a dict
workflow_step_condition_document_attribute_dict = workflow_step_condition_document_attribute_instance.to_dict()
# create an instance of WorkflowStepConditionDocumentAttribute from a dict
workflow_step_condition_document_attribute_from_dict = WorkflowStepConditionDocumentAttribute.from_dict(workflow_step_condition_document_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


