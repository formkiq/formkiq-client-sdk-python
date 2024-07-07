# GetExaminePdfUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Uploaded document identifier | [optional] 
**upload_url** | **str** | Url to upload document to | [optional] 

## Example

```python
from formkiq_client.models.get_examine_pdf_url_response import GetExaminePdfUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetExaminePdfUrlResponse from a JSON string
get_examine_pdf_url_response_instance = GetExaminePdfUrlResponse.from_json(json)
# print the JSON string representation of the object
print(GetExaminePdfUrlResponse.to_json())

# convert the object into a dict
get_examine_pdf_url_response_dict = get_examine_pdf_url_response_instance.to_dict()
# create an instance of GetExaminePdfUrlResponse from a dict
get_examine_pdf_url_response_from_dict = GetExaminePdfUrlResponse.from_dict(get_examine_pdf_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


