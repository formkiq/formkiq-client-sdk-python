# GetActivitesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**activities** | [**List[Activity]**](Activity.md) | List of Entity Type activities | [optional] 

## Example

```python
from formkiq_client.models.get_activites_response import GetActivitesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetActivitesResponse from a JSON string
get_activites_response_instance = GetActivitesResponse.from_json(json)
# print the JSON string representation of the object
print(GetActivitesResponse.to_json())

# convert the object into a dict
get_activites_response_dict = get_activites_response_instance.to_dict()
# create an instance of GetActivitesResponse from a dict
get_activites_response_from_dict = GetActivitesResponse.from_dict(get_activites_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


