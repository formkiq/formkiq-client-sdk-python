# GetAttributeAllowedValuesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_values** | **List[str]** | Attribute&#39;s allowed values | [optional] 
**localized_allowed_values** | **Dict[str, str]** |  | [optional] 

## Example

```python
from formkiq_client.models.get_attribute_allowed_values_response import GetAttributeAllowedValuesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAttributeAllowedValuesResponse from a JSON string
get_attribute_allowed_values_response_instance = GetAttributeAllowedValuesResponse.from_json(json)
# print the JSON string representation of the object
print(GetAttributeAllowedValuesResponse.to_json())

# convert the object into a dict
get_attribute_allowed_values_response_dict = get_attribute_allowed_values_response_instance.to_dict()
# create an instance of GetAttributeAllowedValuesResponse from a dict
get_attribute_allowed_values_response_from_dict = GetAttributeAllowedValuesResponse.from_dict(get_attribute_allowed_values_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


