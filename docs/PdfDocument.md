# PdfDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[PdfDocumentField]**](PdfDocumentField.md) | List of document fields | [optional] 

## Example

```python
from openapi_client.models.pdf_document import PdfDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PdfDocument from a JSON string
pdf_document_instance = PdfDocument.from_json(json)
# print the JSON string representation of the object
print(PdfDocument.to_json())

# convert the object into a dict
pdf_document_dict = pdf_document_instance.to_dict()
# create an instance of PdfDocument from a dict
pdf_document_from_dict = PdfDocument.from_dict(pdf_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


