# SiteConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_content_length_bytes** | **str** | Set Maximum Document Content Length in Bytes | [optional] 
**max_documents** | **str** | Set Maximum number of Documents allowed | [optional] 
**max_webhooks** | **str** | Set Maximum number of Webhooks allowed | [optional] 
**ocr** | [**OcrConfig**](OcrConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.site_config import SiteConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SiteConfig from a JSON string
site_config_instance = SiteConfig.from_json(json)
# print the JSON string representation of the object
print(SiteConfig.to_json())

# convert the object into a dict
site_config_dict = site_config_instance.to_dict()
# create an instance of SiteConfig from a dict
site_config_from_dict = SiteConfig.from_dict(site_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


