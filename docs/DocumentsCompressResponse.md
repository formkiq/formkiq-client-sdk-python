# DocumentsCompressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | Archive download URL | [optional] 

## Example

```python
from formkiq_client.models.documents_compress_response import DocumentsCompressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsCompressResponse from a JSON string
documents_compress_response_instance = DocumentsCompressResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentsCompressResponse.to_json())

# convert the object into a dict
documents_compress_response_dict = documents_compress_response_instance.to_dict()
# create an instance of DocumentsCompressResponse from a dict
documents_compress_response_form_dict = documents_compress_response.from_dict(documents_compress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


