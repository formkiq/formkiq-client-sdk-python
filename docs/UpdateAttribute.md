# UpdateAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AttributeType**](AttributeType.md) |  | [optional] [default to AttributeType.STANDARD]
**watermark** | [**Watermark**](Watermark.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_attribute import UpdateAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAttribute from a JSON string
update_attribute_instance = UpdateAttribute.from_json(json)
# print the JSON string representation of the object
print(UpdateAttribute.to_json())

# convert the object into a dict
update_attribute_dict = update_attribute_instance.to_dict()
# create an instance of UpdateAttribute from a dict
update_attribute_from_dict = UpdateAttribute.from_dict(update_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


