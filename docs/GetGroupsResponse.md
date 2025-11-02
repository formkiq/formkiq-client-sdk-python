# GetGroupsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**groups** | [**List[Group]**](Group.md) | List of groups | [optional] 

## Example

```python
from openapi_client.models.get_groups_response import GetGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsResponse from a JSON string
get_groups_response_instance = GetGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(GetGroupsResponse.to_json())

# convert the object into a dict
get_groups_response_dict = get_groups_response_instance.to_dict()
# create an instance of GetGroupsResponse from a dict
get_groups_response_from_dict = GetGroupsResponse.from_dict(get_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


