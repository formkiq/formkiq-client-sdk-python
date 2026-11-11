# SetGroupPermissionsRequest

Replaces the group's grants for a site. roleType is optional. Supply a predefined roleType with no permissions or an empty array, or CUSTOM with a nonempty permissions array. Nonempty permissions with a predefined roleType are rejected. When roleType is omitted, a nonempty permissions array is required and is treated as an explicit CUSTOM grant without adding inherited role permissions. For example, legacy WRITE grants write operations only and is not converted to the predefined WRITE role, which also grants read and delete operations. Requests with neither field, unknown role types or permission names, and invalid field combinations are rejected. Administrator grants require an administrator caller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_type** | [**ApiPermissionRoleType**](ApiPermissionRoleType.md) |  | [optional] 
**permissions** | [**List[ApiPermissionGrant]**](ApiPermissionGrant.md) | Explicit scoped or legacy umbrella grants. Required when roleType is omitted or CUSTOM, and must then be nonempty. For predefined role types, omit this field or supply an empty array. | [optional] 

## Example

```python
from formkiq_client.models.set_group_permissions_request import SetGroupPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetGroupPermissionsRequest from a JSON string
set_group_permissions_request_instance = SetGroupPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(SetGroupPermissionsRequest.to_json())

# convert the object into a dict
set_group_permissions_request_dict = set_group_permissions_request_instance.to_dict()
# create an instance of SetGroupPermissionsRequest from a dict
set_group_permissions_request_from_dict = SetGroupPermissionsRequest.from_dict(set_group_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


