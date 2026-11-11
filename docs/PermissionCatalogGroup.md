# PermissionCatalogGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**ApiPermissionGroup**](ApiPermissionGroup.md) |  | 
**label** | **str** | Display label for the permission group | 
**permissions** | [**List[PermissionCatalogPermission]**](PermissionCatalogPermission.md) | Scoped permissions and their descriptions in this group | 

## Example

```python
from formkiq_client.models.permission_catalog_group import PermissionCatalogGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionCatalogGroup from a JSON string
permission_catalog_group_instance = PermissionCatalogGroup.from_json(json)
# print the JSON string representation of the object
print(PermissionCatalogGroup.to_json())

# convert the object into a dict
permission_catalog_group_dict = permission_catalog_group_instance.to_dict()
# create an instance of PermissionCatalogGroup from a dict
permission_catalog_group_from_dict = PermissionCatalogGroup.from_dict(permission_catalog_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


