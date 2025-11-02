# GetSiteGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**SiteGroup**](SiteGroup.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_site_group_response import GetSiteGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSiteGroupResponse from a JSON string
get_site_group_response_instance = GetSiteGroupResponse.from_json(json)
# print the JSON string representation of the object
print(GetSiteGroupResponse.to_json())

# convert the object into a dict
get_site_group_response_dict = get_site_group_response_instance.to_dict()
# create an instance of GetSiteGroupResponse from a dict
get_site_group_response_from_dict = GetSiteGroupResponse.from_dict(get_site_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


