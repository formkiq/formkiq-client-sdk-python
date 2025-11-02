# UpdateDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path or Name of document | [optional] 
**width** | **str** | Document Content Width property | [optional] 
**height** | **str** | Document Content Height property | [optional] 
**deep_link_path** | **str** | Path or Name of deep link | [optional] 
**content_type** | **str** | Document media type | [optional] 
**is_base64** | **bool** | Is the content Base64-encoded? | [optional] 
**content** | **str** | Document content | [optional] 
**checksum** | **str** | Document checksum, changes when document file changes | [optional] 
**checksum_type** | [**ChecksumType**](ChecksumType.md) |  | [optional] 
**tags** | [**List[AddDocumentTag]**](AddDocumentTag.md) | List of document tags | [optional] 
**metadata** | [**List[AddDocumentMetadata]**](AddDocumentMetadata.md) | List of document Metadata | [optional] 
**attributes** | [**List[AddDocumentAttribute]**](AddDocumentAttribute.md) | List of document attributes | [optional] 
**actions** | [**List[AddAction]**](AddAction.md) | List of Actions | [optional] 
**documents** | [**List[AddChildDocument]**](AddChildDocument.md) | List of child documents | [optional] 

## Example

```python
from openapi_client.model.update_document_request import UpdateDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDocumentRequest from a JSON string
update_document_request_instance = UpdateDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDocumentRequest.to_json())

# convert the object into a dict
update_document_request_dict = update_document_request_instance.to_dict()
# create an instance of UpdateDocumentRequest from a dict
update_document_request_from_dict = UpdateDocumentRequest.from_dict(update_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


