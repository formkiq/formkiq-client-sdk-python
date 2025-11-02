# AddFolderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path of Folder to create | [optional] 

## Example

```python
from openapi_client.model.add_folder_request import AddFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddFolderRequest from a JSON string
add_folder_request_instance = AddFolderRequest.from_json(json)
# print the JSON string representation of the object
print(AddFolderRequest.to_json())

# convert the object into a dict
add_folder_request_dict = add_folder_request_instance.to_dict()
# create an instance of AddFolderRequest from a dict
add_folder_request_from_dict = AddFolderRequest.from_dict(add_folder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


