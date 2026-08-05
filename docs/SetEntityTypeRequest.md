# SetEntityTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | [**AddEntityType**](AddEntityType.md) |  | [optional] 

## Example

```python
from formkiq_client.models.set_entity_type_request import SetEntityTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetEntityTypeRequest from a JSON string
set_entity_type_request_instance = SetEntityTypeRequest.from_json(json)
# print the JSON string representation of the object
print(SetEntityTypeRequest.to_json())

# convert the object into a dict
set_entity_type_request_dict = set_entity_type_request_instance.to_dict()
# create an instance of SetEntityTypeRequest from a dict
set_entity_type_request_from_dict = SetEntityTypeRequest.from_dict(set_entity_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


