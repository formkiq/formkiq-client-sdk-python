# OcrTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **List[str]** |  | [optional] 
**data** | **List[List[OcrTableData]]** |  | [optional] 

## Example

```python
from formkiq_client.models.ocr_table import OcrTable

# TODO update the JSON string below
json = "{}"
# create an instance of OcrTable from a JSON string
ocr_table_instance = OcrTable.from_json(json)
# print the JSON string representation of the object
print(OcrTable.to_json())

# convert the object into a dict
ocr_table_dict = ocr_table_instance.to_dict()
# create an instance of OcrTable from a dict
ocr_table_from_dict = OcrTable.from_dict(ocr_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


