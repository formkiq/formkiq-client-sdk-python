# BrandingConfig

Branding configuration that can be set globally or for an individual site.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**theme** | **str** | Branding theme identifier. | [optional] 

## Example

```python
from formkiq_client.models.branding_config import BrandingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingConfig from a JSON string
branding_config_instance = BrandingConfig.from_json(json)
# print the JSON string representation of the object
print(BrandingConfig.to_json())

# convert the object into a dict
branding_config_dict = branding_config_instance.to_dict()
# create an instance of BrandingConfig from a dict
branding_config_from_dict = BrandingConfig.from_dict(branding_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


