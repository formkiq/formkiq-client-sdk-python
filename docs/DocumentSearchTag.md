# DocumentSearchTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begins_with** | **str** | Searches for strings that begin with | [optional] 
**eq** | **str** | Searches for strings that eq | [optional] 
**eq_or** | **List[str]** | Searches for ANY strings that eq | [optional] 
**key** | **str** | Tag key to search | 

## Example

```python
from formkiq_client.models.document_search_tag import DocumentSearchTag

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchTag from a JSON string
document_search_tag_instance = DocumentSearchTag.from_json(json)
# print the JSON string representation of the object
print DocumentSearchTag.to_json()

# convert the object into a dict
document_search_tag_dict = document_search_tag_instance.to_dict()
# create an instance of DocumentSearchTag from a dict
document_search_tag_form_dict = document_search_tag.from_dict(document_search_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


