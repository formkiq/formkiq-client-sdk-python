# AddDocumentTagsRequest

Add List of document tags

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[AddDocumentTag]**](AddDocumentTag.md) | List of document tags | [optional] 

## Example

```python
from openapi_client.models.add_document_tags_request import AddDocumentTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentTagsRequest from a JSON string
add_document_tags_request_instance = AddDocumentTagsRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentTagsRequest.to_json())

# convert the object into a dict
add_document_tags_request_dict = add_document_tags_request_instance.to_dict()
# create an instance of AddDocumentTagsRequest from a dict
add_document_tags_request_from_dict = AddDocumentTagsRequest.from_dict(add_document_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


