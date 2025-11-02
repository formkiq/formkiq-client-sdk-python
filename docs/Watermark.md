# Watermark


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**font_size** | **float** | Watermark Font Size | [optional] 
**text** | **str** | Watermark text | [optional] 
**rotation** | **float** | Watermark Rotation | [optional] 
**image_document_id** | **str** | Watermark Image Document Id | [optional] 
**scale** | [**WatermarkScale**](WatermarkScale.md) |  | [optional] 
**position** | [**WatermarkPosition**](WatermarkPosition.md) |  | [optional] 

## Example

```python
from openapi_client.models.watermark import Watermark

# TODO update the JSON string below
json = "{}"
# create an instance of Watermark from a JSON string
watermark_instance = Watermark.from_json(json)
# print the JSON string representation of the object
print(Watermark.to_json())

# convert the object into a dict
watermark_dict = watermark_instance.to_dict()
# create an instance of Watermark from a dict
watermark_from_dict = Watermark.from_dict(watermark_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


