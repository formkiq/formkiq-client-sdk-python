# ActivityDelegation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used_by_user_id** | **str** | User who used the delegation token for the activity | [optional] 
**reason** | **str** | Reason supplied when the delegation token was generated | [optional] 

## Example

```python
from formkiq_client.models.activity_delegation import ActivityDelegation

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityDelegation from a JSON string
activity_delegation_instance = ActivityDelegation.from_json(json)
# print the JSON string representation of the object
print(ActivityDelegation.to_json())

# convert the object into a dict
activity_delegation_dict = activity_delegation_instance.to_dict()
# create an instance of ActivityDelegation from a dict
activity_delegation_from_dict = ActivityDelegation.from_dict(activity_delegation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


