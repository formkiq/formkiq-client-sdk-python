# GetUserGroupsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**groups** | [**List[Group]**](Group.md) | List of groups | [optional] 

## Example

```python
from formkiq_client.models.get_user_groups_response import GetUserGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserGroupsResponse from a JSON string
get_user_groups_response_instance = GetUserGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserGroupsResponse.to_json())

# convert the object into a dict
get_user_groups_response_dict = get_user_groups_response_instance.to_dict()
# create an instance of GetUserGroupsResponse from a dict
get_user_groups_response_from_dict = GetUserGroupsResponse.from_dict(get_user_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


