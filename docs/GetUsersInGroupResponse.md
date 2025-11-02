# GetUsersInGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**users** | [**List[User]**](User.md) | List of users | [optional] 

## Example

```python
from openapi_client.models.get_users_in_group_response import GetUsersInGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsersInGroupResponse from a JSON string
get_users_in_group_response_instance = GetUsersInGroupResponse.from_json(json)
# print the JSON string representation of the object
print(GetUsersInGroupResponse.to_json())

# convert the object into a dict
get_users_in_group_response_dict = get_users_in_group_response_instance.to_dict()
# create an instance of GetUsersInGroupResponse from a dict
get_users_in_group_response_from_dict = GetUsersInGroupResponse.from_dict(get_users_in_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


