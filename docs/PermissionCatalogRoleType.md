# PermissionCatalogRoleType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**ApiPermissionRoleType**](ApiPermissionRoleType.md) |  | 
**groups** | [**List[PermissionCatalogGroup]**](PermissionCatalogGroup.md) | Nonempty groups of effective permissions for a predefined role type. For CUSTOM, these groups contain all selectable scoped permissions. | 

## Example

```python
from formkiq_client.models.permission_catalog_role_type import PermissionCatalogRoleType

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionCatalogRoleType from a JSON string
permission_catalog_role_type_instance = PermissionCatalogRoleType.from_json(json)
# print the JSON string representation of the object
print(PermissionCatalogRoleType.to_json())

# convert the object into a dict
permission_catalog_role_type_dict = permission_catalog_role_type_instance.to_dict()
# create an instance of PermissionCatalogRoleType from a dict
permission_catalog_role_type_from_dict = PermissionCatalogRoleType.from_dict(permission_catalog_role_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


