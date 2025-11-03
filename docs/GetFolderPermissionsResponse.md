# GetFolderPermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[FolderPermission]**](FolderPermission.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_folder_permissions_response import GetFolderPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFolderPermissionsResponse from a JSON string
get_folder_permissions_response_instance = GetFolderPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetFolderPermissionsResponse.to_json())

# convert the object into a dict
get_folder_permissions_response_dict = get_folder_permissions_response_instance.to_dict()
# create an instance of GetFolderPermissionsResponse from a dict
get_folder_permissions_response_from_dict = GetFolderPermissionsResponse.from_dict(get_folder_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


