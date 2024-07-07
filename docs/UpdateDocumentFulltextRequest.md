# UpdateDocumentFulltextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | Document Content-Type | [optional] 
**content** | **str** | Document content | [optional] 
**content_urls** | **List[str]** | URL(s) which contain document content | [optional] 
**path** | **str** | Path or Name of document | [optional] 
**deep_link_path** | **str** | Path or Name of deep link | [optional] 
**tags** | [**List[AddDocumentTag]**](AddDocumentTag.md) | List of document tags | [optional] 
**metadata** | [**List[AddDocumentMetadata]**](AddDocumentMetadata.md) | List of document Metadata | [optional] 

## Example

```python
from formkiq_client.models.update_document_fulltext_request import UpdateDocumentFulltextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDocumentFulltextRequest from a JSON string
update_document_fulltext_request_instance = UpdateDocumentFulltextRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDocumentFulltextRequest.to_json())

# convert the object into a dict
update_document_fulltext_request_dict = update_document_fulltext_request_instance.to_dict()
# create an instance of UpdateDocumentFulltextRequest from a dict
update_document_fulltext_request_from_dict = UpdateDocumentFulltextRequest.from_dict(update_document_fulltext_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


