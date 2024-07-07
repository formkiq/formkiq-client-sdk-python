# AddDocumentUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_schema_id** | **str** | Tag Schema Id | [optional] 
**path** | **str** | Path or Name of document | [optional] 
**content_type** | **str** | Document media type | [optional] 
**deep_link_path** | **str** | Path or Name of deep link | [optional] 
**attributes** | [**List[AddDocumentAttribute]**](AddDocumentAttribute.md) | List of Attributes to add to document | [optional] 
**tags** | [**List[AddDocumentTag]**](AddDocumentTag.md) | List of document tags | [optional] 
**actions** | [**List[AddAction]**](AddAction.md) | List of Actions | [optional] 

## Example

```python
from formkiq_client.models.add_document_upload_request import AddDocumentUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentUploadRequest from a JSON string
add_document_upload_request_instance = AddDocumentUploadRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentUploadRequest.to_json())

# convert the object into a dict
add_document_upload_request_dict = add_document_upload_request_instance.to_dict()
# create an instance of AddDocumentUploadRequest from a dict
add_document_upload_request_from_dict = AddDocumentUploadRequest.from_dict(add_document_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


