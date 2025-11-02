# AddFolderPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** | Name of Role | [optional] 
**permissions** | [**List[FolderPermissionType]**](FolderPermissionType.md) | List of permissions | [optional] 

## Example

```python
from openapi_client.model.add_folder_permission import AddFolderPermission

# TODO update the JSON string below
json = "{}"
# create an instance of AddFolderPermission from a JSON string
add_folder_permission_instance = AddFolderPermission.from_json(json)
# print the JSON string representation of the object
print(AddFolderPermission.to_json())

# convert the object into a dict
add_folder_permission_dict = add_folder_permission_instance.to_dict()
# create an instance of AddFolderPermission from a dict
add_folder_permission_from_dict = AddFolderPermission.from_dict(add_folder_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


