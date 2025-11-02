# AddDocumentOcrRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**textract_queries** | [**List[TextractQuery]**](TextractQuery.md) |  | [optional] 
**parse_types** | **List[str]** | OCR Parse types - TEXT, FORMS, TABLES, QUERIES | [optional] 
**add_pdf_detected_characters_as_text** | **bool** | Rewrite PDF document, converting any Image text to searchable text | [optional] 
**ocr_engine** | [**OcrEngine**](OcrEngine.md) |  | [optional] 
**ocr_number_of_pages** | **str** | Number of pages to OCR (from start) (-1 all) | [optional] 
**ocr_output_type** | [**OcrOutputType**](OcrOutputType.md) |  | [optional] 

## Example

```python
from formkiq_client.models.add_document_ocr_request import AddDocumentOcrRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentOcrRequest from a JSON string
add_document_ocr_request_instance = AddDocumentOcrRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentOcrRequest.to_json())

# convert the object into a dict
add_document_ocr_request_dict = add_document_ocr_request_instance.to_dict()
# create an instance of AddDocumentOcrRequest from a dict
add_document_ocr_request_from_dict = AddDocumentOcrRequest.from_dict(add_document_ocr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


