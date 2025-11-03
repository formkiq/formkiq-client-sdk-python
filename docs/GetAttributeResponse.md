# GetAttributeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**Attribute**](Attribute.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_attribute_response import GetAttributeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAttributeResponse from a JSON string
get_attribute_response_instance = GetAttributeResponse.from_json(json)
# print the JSON string representation of the object
print(GetAttributeResponse.to_json())

# convert the object into a dict
get_attribute_response_dict = get_attribute_response_instance.to_dict()
# create an instance of GetAttributeResponse from a dict
get_attribute_response_from_dict = GetAttributeResponse.from_dict(get_attribute_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


