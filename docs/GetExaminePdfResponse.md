# GetExaminePdfResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileinfo** | [**PdfDocument**](PdfDocument.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_examine_pdf_response import GetExaminePdfResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetExaminePdfResponse from a JSON string
get_examine_pdf_response_instance = GetExaminePdfResponse.from_json(json)
# print the JSON string representation of the object
print(GetExaminePdfResponse.to_json())

# convert the object into a dict
get_examine_pdf_response_dict = get_examine_pdf_response_instance.to_dict()
# create an instance of GetExaminePdfResponse from a dict
get_examine_pdf_response_form_dict = get_examine_pdf_response.from_dict(get_examine_pdf_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


