# MoveFolderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Folder move request status message | [optional] 

## Example

```python
from formkiq_client.models.move_folder_response import MoveFolderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MoveFolderResponse from a JSON string
move_folder_response_instance = MoveFolderResponse.from_json(json)
# print the JSON string representation of the object
print(MoveFolderResponse.to_json())

# convert the object into a dict
move_folder_response_dict = move_folder_response_instance.to_dict()
# create an instance of MoveFolderResponse from a dict
move_folder_response_from_dict = MoveFolderResponse.from_dict(move_folder_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


