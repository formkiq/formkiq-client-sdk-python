# AddFolderShareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share** | [**AddShare**](AddShare.md) |  | [optional] 

## Example

```python
from formkiq_client.models.add_folder_share_request import AddFolderShareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddFolderShareRequest from a JSON string
add_folder_share_request_instance = AddFolderShareRequest.from_json(json)
# print the JSON string representation of the object
print(AddFolderShareRequest.to_json())

# convert the object into a dict
add_folder_share_request_dict = add_folder_share_request_instance.to_dict()
# create an instance of AddFolderShareRequest from a dict
add_folder_share_request_from_dict = AddFolderShareRequest.from_dict(add_folder_share_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


