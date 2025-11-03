# AddEntityTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | [**AddEntityType**](AddEntityType.md) |  | [optional] 

## Example

```python
from formkiq_client.models.add_entity_type_request import AddEntityTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddEntityTypeRequest from a JSON string
add_entity_type_request_instance = AddEntityTypeRequest.from_json(json)
# print the JSON string representation of the object
print(AddEntityTypeRequest.to_json())

# convert the object into a dict
add_entity_type_request_dict = add_entity_type_request_instance.to_dict()
# create an instance of AddEntityTypeRequest from a dict
add_entity_type_request_from_dict = AddEntityTypeRequest.from_dict(add_entity_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


