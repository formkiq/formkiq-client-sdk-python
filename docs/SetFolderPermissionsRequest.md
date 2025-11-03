# SetFolderPermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path of Folder | [optional] 
**roles** | [**List[AddFolderPermission]**](AddFolderPermission.md) |  | [optional] 

## Example

```python
from formkiq_client.models.set_folder_permissions_request import SetFolderPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetFolderPermissionsRequest from a JSON string
set_folder_permissions_request_instance = SetFolderPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(SetFolderPermissionsRequest.to_json())

# convert the object into a dict
set_folder_permissions_request_dict = set_folder_permissions_request_instance.to_dict()
# create an instance of SetFolderPermissionsRequest from a dict
set_folder_permissions_request_from_dict = SetFolderPermissionsRequest.from_dict(set_folder_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


