# Locale


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | ISO 639-1 language code (eg: en (English), fr (French), de (German)) | [optional] 
**country** | **str** | ISO 3166-1 country code (eg: US, CA, DE, FR) | [optional] 

## Example

```python
from formkiq_client.models.locale import Locale

# TODO update the JSON string below
json = "{}"
# create an instance of Locale from a JSON string
locale_instance = Locale.from_json(json)
# print the JSON string representation of the object
print(Locale.to_json())

# convert the object into a dict
locale_dict = locale_instance.to_dict()
# create an instance of Locale from a dict
locale_from_dict = Locale.from_dict(locale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

