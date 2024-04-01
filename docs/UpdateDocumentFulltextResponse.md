# UpdateDocumentFulltextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Full text processing message | [optional] 

## Example

```python
from formkiq_client.models.update_document_fulltext_response import UpdateDocumentFulltextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDocumentFulltextResponse from a JSON string
update_document_fulltext_response_instance = UpdateDocumentFulltextResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateDocumentFulltextResponse.to_json())

# convert the object into a dict
update_document_fulltext_response_dict = update_document_fulltext_response_instance.to_dict()
# create an instance of UpdateDocumentFulltextResponse from a dict
update_document_fulltext_response_form_dict = update_document_fulltext_response.from_dict(update_document_fulltext_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


