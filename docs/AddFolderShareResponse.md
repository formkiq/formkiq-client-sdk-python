# AddFolderShareResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | API Response message | [optional] 
**share_key** | **str** | Share Identifier | [optional] 

## Example

```python
from formkiq_client.models.add_folder_share_response import AddFolderShareResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddFolderShareResponse from a JSON string
add_folder_share_response_instance = AddFolderShareResponse.from_json(json)
# print the JSON string representation of the object
print AddFolderShareResponse.to_json()

# convert the object into a dict
add_folder_share_response_dict = add_folder_share_response_instance.to_dict()
# create an instance of AddFolderShareResponse from a dict
add_folder_share_response_form_dict = add_folder_share_response.from_dict(add_folder_share_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


