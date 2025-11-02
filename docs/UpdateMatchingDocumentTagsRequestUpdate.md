# UpdateMatchingDocumentTagsRequestUpdate

Data to update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[AddDocumentTag]**](AddDocumentTag.md) | List of document tags | [optional] 

## Example

```python
from openapi_client.model.update_matching_document_tags_request_update import UpdateMatchingDocumentTagsRequestUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMatchingDocumentTagsRequestUpdate from a JSON string
update_matching_document_tags_request_update_instance = UpdateMatchingDocumentTagsRequestUpdate.from_json(json)
# print the JSON string representation of the object
print(UpdateMatchingDocumentTagsRequestUpdate.to_json())

# convert the object into a dict
update_matching_document_tags_request_update_dict = update_matching_document_tags_request_update_instance.to_dict()
# create an instance of UpdateMatchingDocumentTagsRequestUpdate from a dict
update_matching_document_tags_request_update_from_dict = UpdateMatchingDocumentTagsRequestUpdate.from_dict(update_matching_document_tags_request_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


