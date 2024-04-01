# DocumentSearchMatchTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Tag key | [optional] 
**value** | **str** | Tag value | [optional] 
**type** | **str** | Tag type | [optional] 

## Example

```python
from formkiq_client.models.document_search_match_tag import DocumentSearchMatchTag

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchMatchTag from a JSON string
document_search_match_tag_instance = DocumentSearchMatchTag.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchMatchTag.to_json())

# convert the object into a dict
document_search_match_tag_dict = document_search_match_tag_instance.to_dict()
# create an instance of DocumentSearchMatchTag from a dict
document_search_match_tag_form_dict = document_search_match_tag.from_dict(document_search_match_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


