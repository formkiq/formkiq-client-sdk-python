# PdfDocumentField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Name of Field | [optional] 
**value** | **str** | Value of Field | [optional] 

## Example

```python
from openapi_client.models.pdf_document_field import PdfDocumentField

# TODO update the JSON string below
json = "{}"
# create an instance of PdfDocumentField from a JSON string
pdf_document_field_instance = PdfDocumentField.from_json(json)
# print the JSON string representation of the object
print(PdfDocumentField.to_json())

# convert the object into a dict
pdf_document_field_dict = pdf_document_field_instance.to_dict()
# create an instance of PdfDocumentField from a dict
pdf_document_field_from_dict = PdfDocumentField.from_dict(pdf_document_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


