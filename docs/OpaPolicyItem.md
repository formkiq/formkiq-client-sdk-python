# OpaPolicyItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**OpaPolicyItemType**](OpaPolicyItemType.md) |  | [optional] 
**policy** | **str** | OPA Policy in REGO format | [optional] 
**all_roles** | **List[str]** | User must match all roles | [optional] 
**any_roles** | **List[str]** | User must match any role | [optional] 
**attributes** | [**List[OpaPolicyAttribute]**](OpaPolicyAttribute.md) |  | [optional] 

## Example

```python
from formkiq_client.models.opa_policy_item import OpaPolicyItem

# TODO update the JSON string below
json = "{}"
# create an instance of OpaPolicyItem from a JSON string
opa_policy_item_instance = OpaPolicyItem.from_json(json)
# print the JSON string representation of the object
print(OpaPolicyItem.to_json())

# convert the object into a dict
opa_policy_item_dict = opa_policy_item_instance.to_dict()
# create an instance of OpaPolicyItem from a dict
opa_policy_item_from_dict = OpaPolicyItem.from_dict(opa_policy_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


