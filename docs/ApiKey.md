# ApiKey

An API key and its permission configuration. roleType is optional for legacy records. A missing roleType means permissions contains explicit CUSTOM grants. A predefined roleType determines the effective role grants, which can be discovered in the catalog.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of API Key | [optional] 
**api_key** | **str** | API Key value | [optional] 
**user_id** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**role_type** | [**ApiPermissionRoleType**](ApiPermissionRoleType.md) |  | [optional] 
**permissions** | [**List[ApiPermissionGrant]**](ApiPermissionGrant.md) | Explicit CUSTOM or legacy permission grants. | [optional] 
**groups** | **List[str]** | List of groups to add as custom claims to API Key | [optional] 
**custom_claims** | **Dict[str, object]** | Custom claims associated with the API key and exposed in the requesting caller&#39;s userClaims. Values may be strings, numbers, Booleans, arrays, or objects. Null-valued object fields are omitted. These claims do not override the key&#39;s username, site, groups, role, or permissions. Keys created without custom claims have an empty claims map. | [optional] 

## Example

```python
from formkiq_client.models.api_key import ApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKey from a JSON string
api_key_instance = ApiKey.from_json(json)
# print the JSON string representation of the object
print(ApiKey.to_json())

# convert the object into a dict
api_key_dict = api_key_instance.to_dict()
# create an instance of ApiKey from a dict
api_key_from_dict = ApiKey.from_dict(api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


