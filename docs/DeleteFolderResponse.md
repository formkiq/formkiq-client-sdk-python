# DeleteFolderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | API Response message | [optional] 

## Example

```python
from formkiq_client.models.delete_folder_response import DeleteFolderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFolderResponse from a JSON string
delete_folder_response_instance = DeleteFolderResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteFolderResponse.to_json())

# convert the object into a dict
delete_folder_response_dict = delete_folder_response_instance.to_dict()
# create an instance of DeleteFolderResponse from a dict
delete_folder_response_form_dict = delete_folder_response.from_dict(delete_folder_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


