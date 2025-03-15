# AddLocaleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | Name of Locale | [optional] 

## Example

```python
from formkiq_client.models.add_locale_request import AddLocaleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddLocaleRequest from a JSON string
add_locale_request_instance = AddLocaleRequest.from_json(json)
# print the JSON string representation of the object
print(AddLocaleRequest.to_json())

# convert the object into a dict
add_locale_request_dict = add_locale_request_instance.to_dict()
# create an instance of AddLocaleRequest from a dict
add_locale_request_from_dict = AddLocaleRequest.from_dict(add_locale_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


