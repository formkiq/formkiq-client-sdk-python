# DocumentSearchFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begins_with** | **str** | Searches for a folder | [optional] 

## Example

```python
from formkiq_client.models.document_search_folder import DocumentSearchFolder

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchFolder from a JSON string
document_search_folder_instance = DocumentSearchFolder.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchFolder.to_json())

# convert the object into a dict
document_search_folder_dict = document_search_folder_instance.to_dict()
# create an instance of DocumentSearchFolder from a dict
document_search_folder_from_dict = DocumentSearchFolder.from_dict(document_search_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


