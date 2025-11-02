# GetUserActivitesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**user_activities** | [**List[UserActivity]**](UserActivity.md) | List of user activities | [optional] 

## Example

```python
from openapi_client.models.get_user_activites_response import GetUserActivitesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserActivitesResponse from a JSON string
get_user_activites_response_instance = GetUserActivitesResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserActivitesResponse.to_json())

# convert the object into a dict
get_user_activites_response_dict = get_user_activites_response_instance.to_dict()
# create an instance of GetUserActivitesResponse from a dict
get_user_activites_response_from_dict = GetUserActivitesResponse.from_dict(get_user_activites_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


