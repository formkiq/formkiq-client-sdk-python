# DocumentCompositeSearchTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **str** | Searches for strings that eq | [optional] 
**key** | **str** | Tag key to search | 

## Example

```python
from formkiq_client.models.document_composite_search_tag import DocumentCompositeSearchTag

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCompositeSearchTag from a JSON string
document_composite_search_tag_instance = DocumentCompositeSearchTag.from_json(json)
# print the JSON string representation of the object
print DocumentCompositeSearchTag.to_json()

# convert the object into a dict
document_composite_search_tag_dict = document_composite_search_tag_instance.to_dict()
# create an instance of DocumentCompositeSearchTag from a dict
document_composite_search_tag_form_dict = document_composite_search_tag.from_dict(document_composite_search_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


