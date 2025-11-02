# DocumentsCompressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_ids** | **List[str]** | Documents to compress | 

## Example

```python
from openapi_client.models.documents_compress_request import DocumentsCompressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsCompressRequest from a JSON string
documents_compress_request_instance = DocumentsCompressRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsCompressRequest.to_json())

# convert the object into a dict
documents_compress_request_dict = documents_compress_request_instance.to_dict()
# create an instance of DocumentsCompressRequest from a dict
documents_compress_request_from_dict = DocumentsCompressRequest.from_dict(documents_compress_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


