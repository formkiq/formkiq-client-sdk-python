# UserShare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | Name of Share Group | [optional] 
**share_key** | **str** | Share Identifier | [optional] 
**type** | **str** | Type of Document | [optional] 
**permissions** | [**List[UserSharePermission]**](UserSharePermission.md) | List of share permissions | [optional] 
**site_id** | **str** | Site Identifier | [optional] 
**path** | **str** | Path or Name of document | [optional] 
**user_id** | **str** | User who created share | [optional] 
**permission_type** | [**UserSharePermissionType**](UserSharePermissionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_share import UserShare

# TODO update the JSON string below
json = "{}"
# create an instance of UserShare from a JSON string
user_share_instance = UserShare.from_json(json)
# print the JSON string representation of the object
print(UserShare.to_json())

# convert the object into a dict
user_share_dict = user_share_instance.to_dict()
# create an instance of UserShare from a dict
user_share_from_dict = UserShare.from_dict(user_share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


