# MatchDocumentTag

Match Document Tag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Tag key | 
**begins_with** | **str** | Searches for strings that begin with | [optional] 
**eq** | **str** | Searches for strings that eq | [optional] 

## Example

```python
from openapi_client.models.match_document_tag import MatchDocumentTag

# TODO update the JSON string below
json = "{}"
# create an instance of MatchDocumentTag from a JSON string
match_document_tag_instance = MatchDocumentTag.from_json(json)
# print the JSON string representation of the object
print(MatchDocumentTag.to_json())

# convert the object into a dict
match_document_tag_dict = match_document_tag_instance.to_dict()
# create an instance of MatchDocumentTag from a dict
match_document_tag_from_dict = MatchDocumentTag.from_dict(match_document_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


