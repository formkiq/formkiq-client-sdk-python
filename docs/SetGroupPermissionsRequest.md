# SetGroupPermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[SiteGroupPermissions]**](SiteGroupPermissions.md) |  | [optional] 

## Example

```python
from openapi_client.models.set_group_permissions_request import SetGroupPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetGroupPermissionsRequest from a JSON string
set_group_permissions_request_instance = SetGroupPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(SetGroupPermissionsRequest.to_json())

# convert the object into a dict
set_group_permissions_request_dict = set_group_permissions_request_instance.to_dict()
# create an instance of SetGroupPermissionsRequest from a dict
set_group_permissions_request_from_dict = SetGroupPermissionsRequest.from_dict(set_group_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


