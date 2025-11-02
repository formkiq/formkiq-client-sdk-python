# DocumentSearchMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | **str** | Searches for a folder | [optional] 
**path** | **str** | Searches for a Path of document | [optional] 
**eq** | **str** | Searches for strings that eq | [optional] 
**index_type** | **str** | Searches in an index | [optional] 
**index_filter_begins_with** | **str** | Returns index records that begins with a particular substring | [optional] 

## Example

```python
from openapi_client.models.document_search_meta import DocumentSearchMeta

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchMeta from a JSON string
document_search_meta_instance = DocumentSearchMeta.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchMeta.to_json())

# convert the object into a dict
document_search_meta_dict = document_search_meta_instance.to_dict()
# create an instance of DocumentSearchMeta from a dict
document_search_meta_from_dict = DocumentSearchMeta.from_dict(document_search_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


