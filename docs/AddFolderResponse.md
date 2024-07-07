# AddFolderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response Message | [optional] 
**index_key** | **str** | Folder Index Key | [optional] 

## Example

```python
from formkiq_client.models.add_folder_response import AddFolderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddFolderResponse from a JSON string
add_folder_response_instance = AddFolderResponse.from_json(json)
# print the JSON string representation of the object
print(AddFolderResponse.to_json())

# convert the object into a dict
add_folder_response_dict = add_folder_response_instance.to_dict()
# create an instance of AddFolderResponse from a dict
add_folder_response_from_dict = AddFolderResponse.from_dict(add_folder_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


