# SetEntityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**AddEntity**](AddEntity.md) |  | [optional] 

## Example

```python
from formkiq_client.models.set_entity_request import SetEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetEntityRequest from a JSON string
set_entity_request_instance = SetEntityRequest.from_json(json)
# print the JSON string representation of the object
print(SetEntityRequest.to_json())

# convert the object into a dict
set_entity_request_dict = set_entity_request_instance.to_dict()
# create an instance of SetEntityRequest from a dict
set_entity_request_from_dict = SetEntityRequest.from_dict(set_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


