# AddDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_schema_id** | **str** | Tag Schema Id | [optional] 
**path** | **str** | Path or Name of document | [optional] 
**deep_link_path** | **str** | Path or Name of deep link | [optional] 
**content_type** | **str** | Document media type | [optional] 
**is_base64** | **bool** | Is the content Base64-encoded? | [optional] 
**content** | **str** | Document content | 
**tags** | [**List[AddDocumentTag]**](AddDocumentTag.md) | List of document tags | [optional] 
**metadata** | [**List[AddDocumentMetadata]**](AddDocumentMetadata.md) | List of document Metadata | [optional] 
**actions** | [**List[AddAction]**](AddAction.md) | List of Actions | [optional] 
**attributes** | [**List[AddDocumentAttribute]**](AddDocumentAttribute.md) | List of Attributes to add to document | [optional] 
**documents** | [**List[AddChildDocument]**](AddChildDocument.md) | List of child documents | [optional] 

## Example

```python
from formkiq_client.models.add_document_request import AddDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentRequest from a JSON string
add_document_request_instance = AddDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentRequest.to_json())

# convert the object into a dict
add_document_request_dict = add_document_request_instance.to_dict()
# create an instance of AddDocumentRequest from a dict
add_document_request_from_dict = AddDocumentRequest.from_dict(add_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


