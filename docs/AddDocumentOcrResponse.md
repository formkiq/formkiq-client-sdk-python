# AddDocumentOcrResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | OCR processing message | [optional] 

## Example

```python
from formkiq_client.models.add_document_ocr_response import AddDocumentOcrResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentOcrResponse from a JSON string
add_document_ocr_response_instance = AddDocumentOcrResponse.from_json(json)
# print the JSON string representation of the object
print AddDocumentOcrResponse.to_json()

# convert the object into a dict
add_document_ocr_response_dict = add_document_ocr_response_instance.to_dict()
# create an instance of AddDocumentOcrResponse from a dict
add_document_ocr_response_form_dict = add_document_ocr_response.from_dict(add_document_ocr_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


