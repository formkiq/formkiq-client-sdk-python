# WatermarkPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x_anchor** | [**WatermarkPositionXAnchor**](WatermarkPositionXAnchor.md) |  | [optional] 
**y_anchor** | [**WatermarkPositionYAnchor**](WatermarkPositionYAnchor.md) |  | [optional] 
**x_offset** | **float** | X offset | [optional] 
**y_offset** | **float** | Y offset | [optional] 

## Example

```python
from formkiq_client.models.watermark_position import WatermarkPosition

# TODO update the JSON string below
json = "{}"
# create an instance of WatermarkPosition from a JSON string
watermark_position_instance = WatermarkPosition.from_json(json)
# print the JSON string representation of the object
print(WatermarkPosition.to_json())

# convert the object into a dict
watermark_position_dict = watermark_position_instance.to_dict()
# create an instance of WatermarkPosition from a dict
watermark_position_from_dict = WatermarkPosition.from_dict(watermark_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


