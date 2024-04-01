# StringFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**StringGeneratorType**](StringGeneratorType.md) |  | [optional] 
**static_value** | **str** | Static Value | [optional] 
**padding** | **int** | Optional padding for AUTO_INCREMENT number | [optional] 

## Example

```python
from formkiq_client.models.string_format import StringFormat

# TODO update the JSON string below
json = "{}"
# create an instance of StringFormat from a JSON string
string_format_instance = StringFormat.from_json(json)
# print the JSON string representation of the object
print(StringFormat.to_json())

# convert the object into a dict
string_format_dict = string_format_instance.to_dict()
# create an instance of StringFormat from a dict
string_format_form_dict = string_format.from_dict(string_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


