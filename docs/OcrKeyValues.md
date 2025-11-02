# OcrKeyValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Ocr Key | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.model.ocr_key_values import OcrKeyValues

# TODO update the JSON string below
json = "{}"
# create an instance of OcrKeyValues from a JSON string
ocr_key_values_instance = OcrKeyValues.from_json(json)
# print the JSON string representation of the object
print(OcrKeyValues.to_json())

# convert the object into a dict
ocr_key_values_dict = ocr_key_values_instance.to_dict()
# create an instance of OcrKeyValues from a dict
ocr_key_values_from_dict = OcrKeyValues.from_dict(ocr_key_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


