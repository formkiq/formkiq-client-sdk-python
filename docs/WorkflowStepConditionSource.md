# WorkflowStepConditionSource

Defines the document-derived source value to evaluate for a workflow condition criterion.  The source identifies where the value comes from before applying the operator. Supported sources include: - a document attribute identified by `attributeKey` - a comparison between a document attribute value and another attribute-derived   value - the document content type - the document path 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** | Document attribute key | 
**source_type** | [**WorkflowStepConditionAttributeValueComparisonSourceType**](WorkflowStepConditionAttributeValueComparisonSourceType.md) |  | 
**value_attribute_key** | **str** | Document attribute key containing the value to compare. | 
**comparison** | [**WorkflowStepConditionAttributeValueComparisonTarget**](WorkflowStepConditionAttributeValueComparisonTarget.md) |  | 

## Example

```python
from formkiq_client.models.workflow_step_condition_source import WorkflowStepConditionSource

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepConditionSource from a JSON string
workflow_step_condition_source_instance = WorkflowStepConditionSource.from_json(json)
# print the JSON string representation of the object
print(WorkflowStepConditionSource.to_json())

# convert the object into a dict
workflow_step_condition_source_dict = workflow_step_condition_source_instance.to_dict()
# create an instance of WorkflowStepConditionSource from a dict
workflow_step_condition_source_from_dict = WorkflowStepConditionSource.from_dict(workflow_step_condition_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


