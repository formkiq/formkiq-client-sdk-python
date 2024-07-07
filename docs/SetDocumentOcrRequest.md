# SetDocumentOcrRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | Document Content-Type | [optional] 
**is_base64** | **bool** | Is the content Base64-encoded? | [optional] 
**content** | **str** | Document content | 

## Example

```python
from formkiq_client.models.set_document_ocr_request import SetDocumentOcrRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDocumentOcrRequest from a JSON string
set_document_ocr_request_instance = SetDocumentOcrRequest.from_json(json)
# print the JSON string representation of the object
print(SetDocumentOcrRequest.to_json())

# convert the object into a dict
set_document_ocr_request_dict = set_document_ocr_request_instance.to_dict()
# create an instance of SetDocumentOcrRequest from a dict
set_document_ocr_request_from_dict = SetDocumentOcrRequest.from_dict(set_document_ocr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


