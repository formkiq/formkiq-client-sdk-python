# FolderPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** | Name of Role | [optional] 
**permissions** | [**List[FolderPermissionType]**](FolderPermissionType.md) |  | [optional] 

## Example

```python
from openapi_client.model.folder_permission import FolderPermission

# TODO update the JSON string below
json = "{}"
# create an instance of FolderPermission from a JSON string
folder_permission_instance = FolderPermission.from_json(json)
# print the JSON string representation of the object
print(FolderPermission.to_json())

# convert the object into a dict
folder_permission_dict = folder_permission_instance.to_dict()
# create an instance of FolderPermission from a dict
folder_permission_from_dict = FolderPermission.from_dict(folder_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


