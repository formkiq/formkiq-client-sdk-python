# SetDocumentFulltextRequest


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
from formkiq_client.models.set_document_fulltext_request import SetDocumentFulltextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDocumentFulltextRequest from a JSON string
set_document_fulltext_request_instance = SetDocumentFulltextRequest.from_json(json)
# print the JSON string representation of the object
print(SetDocumentFulltextRequest.to_json())

# convert the object into a dict
set_document_fulltext_request_dict = set_document_fulltext_request_instance.to_dict()
# create an instance of SetDocumentFulltextRequest from a dict
set_document_fulltext_request_from_dict = SetDocumentFulltextRequest.from_dict(set_document_fulltext_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


