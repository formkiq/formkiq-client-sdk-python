# DocumentSearchFilename


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begins_with** | **str** | Searches for a filename | [optional] 

## Example

```python
from formkiq_client.models.document_search_filename import DocumentSearchFilename

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchFilename from a JSON string
document_search_filename_instance = DocumentSearchFilename.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchFilename.to_json())

# convert the object into a dict
document_search_filename_dict = document_search_filename_instance.to_dict()
# create an instance of DocumentSearchFilename from a dict
document_search_filename_from_dict = DocumentSearchFilename.from_dict(document_search_filename_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


