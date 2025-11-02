# GetGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**Group**](Group.md) |  | [optional] 

## Example

```python
from openapi_client.model.get_group_response import GetGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupResponse from a JSON string
get_group_response_instance = GetGroupResponse.from_json(json)
# print the JSON string representation of the object
print(GetGroupResponse.to_json())

# convert the object into a dict
get_group_response_dict = get_group_response_instance.to_dict()
# create an instance of GetGroupResponse from a dict
get_group_response_from_dict = GetGroupResponse.from_dict(get_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


