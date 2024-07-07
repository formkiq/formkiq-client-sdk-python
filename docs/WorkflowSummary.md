# WorkflowSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Workflow | [optional] 
**workflow_id** | **str** | Workflow identifier | [optional] 
**description** | **str** | Description of Workflow | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**user_id** | **str** | User who created workflow | [optional] 
**in_use** | **bool** | Whether the Workflow is in use | [optional] 
**status** | [**WorkflowStatus**](WorkflowStatus.md) |  | [optional] 

## Example

```python
from formkiq_client.models.workflow_summary import WorkflowSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSummary from a JSON string
workflow_summary_instance = WorkflowSummary.from_json(json)
# print the JSON string representation of the object
print(WorkflowSummary.to_json())

# convert the object into a dict
workflow_summary_dict = workflow_summary_instance.to_dict()
# create an instance of WorkflowSummary from a dict
workflow_summary_from_dict = WorkflowSummary.from_dict(workflow_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


