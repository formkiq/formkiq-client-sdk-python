# OcrConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_pages_per_transaction** | **float** | Max number of OCR pages (-1 for unlimited) | [optional] 
**max_transactions** | **float** | Max number of OCR actions that can be created (-1 for unlimited) | [optional] 

## Example

```python
from openapi_client.models.ocr_config import OcrConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OcrConfig from a JSON string
ocr_config_instance = OcrConfig.from_json(json)
# print the JSON string representation of the object
print(OcrConfig.to_json())

# convert the object into a dict
ocr_config_dict = ocr_config_instance.to_dict()
# create an instance of OcrConfig from a dict
ocr_config_from_dict = OcrConfig.from_dict(ocr_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


