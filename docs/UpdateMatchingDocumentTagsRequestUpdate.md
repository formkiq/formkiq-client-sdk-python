# UpdateMatchingDocumentTagsRequestUpdate

Data to update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[AddDocumentTag]**](AddDocumentTag.md) | List of document tags | [optional] 

## Example

```python
from formkiq_client.models.update_matching_document_tags_request_update import UpdateMatchingDocumentTagsRequestUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMatchingDocumentTagsRequestUpdate from a JSON string
update_matching_document_tags_request_update_instance = UpdateMatchingDocumentTagsRequestUpdate.from_json(json)
# print the JSON string representation of the object
print(UpdateMatchingDocumentTagsRequestUpdate.to_json())

# convert the object into a dict
update_matching_document_tags_request_update_dict = update_matching_document_tags_request_update_instance.to_dict()
# create an instance of UpdateMatchingDocumentTagsRequestUpdate from a dict
update_matching_document_tags_request_update_form_dict = update_matching_document_tags_request_update.from_dict(update_matching_document_tags_request_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


