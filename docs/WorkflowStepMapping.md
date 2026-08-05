# WorkflowStepMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping_id** | **str** | Mapping Identifier | 

## Example

```python
from formkiq_client.models.workflow_step_mapping import WorkflowStepMapping

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepMapping from a JSON string
workflow_step_mapping_instance = WorkflowStepMapping.from_json(json)
# print the JSON string representation of the object
print(WorkflowStepMapping.to_json())

# convert the object into a dict
workflow_step_mapping_dict = workflow_step_mapping_instance.to_dict()
# create an instance of WorkflowStepMapping from a dict
workflow_step_mapping_from_dict = WorkflowStepMapping.from_dict(workflow_step_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


