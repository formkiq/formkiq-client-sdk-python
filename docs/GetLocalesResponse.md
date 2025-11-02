# GetLocalesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**locales** | [**List[LocaleInfo]**](LocaleInfo.md) | List of Locale | [optional] 

## Example

```python
from openapi_client.model.get_locales_response import GetLocalesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLocalesResponse from a JSON string
get_locales_response_instance = GetLocalesResponse.from_json(json)
# print the JSON string representation of the object
print(GetLocalesResponse.to_json())

# convert the object into a dict
get_locales_response_dict = get_locales_response_instance.to_dict()
# create an instance of GetLocalesResponse from a dict
get_locales_response_from_dict = GetLocalesResponse.from_dict(get_locales_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


