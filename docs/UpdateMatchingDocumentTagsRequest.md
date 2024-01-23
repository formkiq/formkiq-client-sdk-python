# UpdateMatchingDocumentTagsRequest

Add/Update of multiple document tag(s) based on document(s) that have the matching tag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match** | [**UpdateMatchingDocumentTagsRequestMatch**](UpdateMatchingDocumentTagsRequestMatch.md) |  | 
**update** | [**UpdateMatchingDocumentTagsRequestUpdate**](UpdateMatchingDocumentTagsRequestUpdate.md) |  | 

## Example

```python
from formkiq_client.models.update_matching_document_tags_request import UpdateMatchingDocumentTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMatchingDocumentTagsRequest from a JSON string
update_matching_document_tags_request_instance = UpdateMatchingDocumentTagsRequest.from_json(json)
# print the JSON string representation of the object
print UpdateMatchingDocumentTagsRequest.to_json()

# convert the object into a dict
update_matching_document_tags_request_dict = update_matching_document_tags_request_instance.to_dict()
# create an instance of UpdateMatchingDocumentTagsRequest from a dict
update_matching_document_tags_request_form_dict = update_matching_document_tags_request.from_dict(update_matching_document_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


