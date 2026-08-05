# WorkflowStepConditionCriterion

A single criterion used to evaluate whether a workflow condition matches.  A criterion compares a document-derived source value against one or more provided values using the specified operator.  Supported sources include: - document attributes - document attribute value comparisons - document content type - document path  Typical examples: - attribute `status` equals `approved` - attribute `amount` greater than `1000` - attribute `invoiceTotal` equals attribute `approvedTotal` - attribute `invoiceTotal` equals the sum of attribute `lineItemAmount` - content type equals `application/pdf` - path contains `/invoices/`  Use the appropriate typed value field for the comparison: - `stringValue` for string comparisons - `numberValue` for numeric comparisons - `booleanValue` for boolean comparisons - `stringValues` for multi-value comparisons such as `IN` and `NOT_IN`  Literal value fields should be omitted when `source` is an attribute value comparison. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**WorkflowStepConditionSource**](WorkflowStepConditionSource.md) |  | 
**operator** | [**WorkflowStepConditionOperator**](WorkflowStepConditionOperator.md) |  | 
**string_value** | **str** | String comparison value | [optional] 
**number_value** | **float** | Numeric comparison value | [optional] 
**boolean_value** | **bool** | Boolean comparison value | [optional] 
**string_values** | **List[str]** | String values used for IN or NOT_IN comparisons | [optional] 

## Example

```python
from formkiq_client.models.workflow_step_condition_criterion import WorkflowStepConditionCriterion

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepConditionCriterion from a JSON string
workflow_step_condition_criterion_instance = WorkflowStepConditionCriterion.from_json(json)
# print the JSON string representation of the object
print(WorkflowStepConditionCriterion.to_json())

# convert the object into a dict
workflow_step_condition_criterion_dict = workflow_step_condition_criterion_instance.to_dict()
# create an instance of WorkflowStepConditionCriterion from a dict
workflow_step_condition_criterion_from_dict = WorkflowStepConditionCriterion.from_dict(workflow_step_condition_criterion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


