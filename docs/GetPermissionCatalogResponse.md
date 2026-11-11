# GetPermissionCatalogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_types** | [**List[PermissionCatalogRoleType]**](PermissionCatalogRoleType.md) | Supported role types and their permission groups | 

## Example

```python
from formkiq_client.models.get_permission_catalog_response import GetPermissionCatalogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPermissionCatalogResponse from a JSON string
get_permission_catalog_response_instance = GetPermissionCatalogResponse.from_json(json)
# print the JSON string representation of the object
print(GetPermissionCatalogResponse.to_json())

# convert the object into a dict
get_permission_catalog_response_dict = get_permission_catalog_response_instance.to_dict()
# create an instance of GetPermissionCatalogResponse from a dict
get_permission_catalog_response_from_dict = GetPermissionCatalogResponse.from_dict(get_permission_catalog_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


