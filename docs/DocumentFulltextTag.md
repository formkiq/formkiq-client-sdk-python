# DocumentFulltextTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **str** | Searches for strings that eq | [optional] 
**eq_or** | **List[str]** | Searches for ANY strings that eq | [optional] 
**key** | **str** | Tag key to search | 

## Example

```python
from openapi_client.models.document_fulltext_tag import DocumentFulltextTag

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFulltextTag from a JSON string
document_fulltext_tag_instance = DocumentFulltextTag.from_json(json)
# print the JSON string representation of the object
print(DocumentFulltextTag.to_json())

# convert the object into a dict
document_fulltext_tag_dict = document_fulltext_tag_instance.to_dict()
# create an instance of DocumentFulltextTag from a dict
document_fulltext_tag_from_dict = DocumentFulltextTag.from_dict(document_fulltext_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


