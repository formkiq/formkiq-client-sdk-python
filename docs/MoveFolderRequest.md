# MoveFolderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Target folder path | 

## Example

```python
from formkiq_client.models.move_folder_request import MoveFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MoveFolderRequest from a JSON string
move_folder_request_instance = MoveFolderRequest.from_json(json)
# print the JSON string representation of the object
print(MoveFolderRequest.to_json())

# convert the object into a dict
move_folder_request_dict = move_folder_request_instance.to_dict()
# create an instance of MoveFolderRequest from a dict
move_folder_request_from_dict = MoveFolderRequest.from_dict(move_folder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


