# PermissionCatalogPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**ApiPermission**](ApiPermission.md) |  | 
**description** | **str** | Human-readable explanation of the permission | 

## Example

```python
from formkiq_client.models.permission_catalog_permission import PermissionCatalogPermission

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionCatalogPermission from a JSON string
permission_catalog_permission_instance = PermissionCatalogPermission.from_json(json)
# print the JSON string representation of the object
print(PermissionCatalogPermission.to_json())

# convert the object into a dict
permission_catalog_permission_dict = permission_catalog_permission_instance.to_dict()
# create an instance of PermissionCatalogPermission from a dict
permission_catalog_permission_from_dict = PermissionCatalogPermission.from_dict(permission_catalog_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


