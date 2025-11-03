# AddAttributeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**AddAttribute**](AddAttribute.md) |  | 

## Example

```python
from formkiq_client.models.add_attribute_request import AddAttributeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddAttributeRequest from a JSON string
add_attribute_request_instance = AddAttributeRequest.from_json(json)
# print the JSON string representation of the object
print(AddAttributeRequest.to_json())

# convert the object into a dict
add_attribute_request_dict = add_attribute_request_instance.to_dict()
# create an instance of AddAttributeRequest from a dict
add_attribute_request_from_dict = AddAttributeRequest.from_dict(add_attribute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


