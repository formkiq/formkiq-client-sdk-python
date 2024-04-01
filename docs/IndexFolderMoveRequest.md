# IndexFolderMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source path | [optional] 
**target** | **str** | Target path | [optional] 

## Example

```python
from formkiq_client.models.index_folder_move_request import IndexFolderMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IndexFolderMoveRequest from a JSON string
index_folder_move_request_instance = IndexFolderMoveRequest.from_json(json)
# print the JSON string representation of the object
print(IndexFolderMoveRequest.to_json())

# convert the object into a dict
index_folder_move_request_dict = index_folder_move_request_instance.to_dict()
# create an instance of IndexFolderMoveRequest from a dict
index_folder_move_request_form_dict = index_folder_move_request.from_dict(index_folder_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


