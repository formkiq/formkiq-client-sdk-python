# AddAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Attribute Key | 
**data_type** | [**AttributeDataType**](AttributeDataType.md) |  | [optional] [default to AttributeDataType.STRING]
**type** | [**AttributeType**](AttributeType.md) |  | [optional] [default to AttributeType.STANDARD]

## Example

```python
from formkiq_client.models.add_attribute import AddAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of AddAttribute from a JSON string
add_attribute_instance = AddAttribute.from_json(json)
# print the JSON string representation of the object
print(AddAttribute.to_json())

# convert the object into a dict
add_attribute_dict = add_attribute_instance.to_dict()
# create an instance of AddAttribute from a dict
add_attribute_from_dict = AddAttribute.from_dict(add_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


