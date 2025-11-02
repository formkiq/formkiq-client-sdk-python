# GetSiteGroupsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_names** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.get_site_groups_response import GetSiteGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSiteGroupsResponse from a JSON string
get_site_groups_response_instance = GetSiteGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(GetSiteGroupsResponse.to_json())

# convert the object into a dict
get_site_groups_response_dict = get_site_groups_response_instance.to_dict()
# create an instance of GetSiteGroupsResponse from a dict
get_site_groups_response_from_dict = GetSiteGroupsResponse.from_dict(get_site_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


