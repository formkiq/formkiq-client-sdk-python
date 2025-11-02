# AddEntityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**AddEntity**](AddEntity.md) |  | [optional] 

## Example

```python
from openapi_client.model.add_entity_request import AddEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddEntityRequest from a JSON string
add_entity_request_instance = AddEntityRequest.from_json(json)
# print the JSON string representation of the object
print(AddEntityRequest.to_json())

# convert the object into a dict
add_entity_request_dict = add_entity_request_instance.to_dict()
# create an instance of AddEntityRequest from a dict
add_entity_request_from_dict = AddEntityRequest.from_dict(add_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


