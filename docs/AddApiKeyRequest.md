# AddApiKeyRequest

roleType is optional. A predefined roleType must be supplied without nonempty permissions; an omitted or empty array is accepted. CUSTOM requires a nonempty permissions array. When roleType is omitted, a nonempty permissions array is an explicit CUSTOM grant: legacy WRITE grants write operations only and is not converted to the predefined WRITE role, which also grants read and delete operations. If neither field is supplied, or permissions is empty with no roleType, the legacy READ, WRITE and DELETE defaults apply. Unknown role types or permission names, and invalid field combinations, are rejected. ADMIN roles and ADMIN permission grants are not allowed, even for administrators.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of API Key | 
**groups** | **List[str]** | Optional list of groups to add as custom claims to API Key | [optional] 
**custom_claims** | **Dict[str, object]** | Optional custom application claims to associate with the API key. Values may be strings, numbers, Booleans, arrays, or objects and retain their JSON types. Null-valued object fields are omitted. Claims are exposed through userClaims when authenticating with this key and do not override its username, site, groups, role, or permissions. Omission means no custom claims. | [optional] 
**role_type** | [**ApiPermissionRoleType**](ApiPermissionRoleType.md) |  | [optional] 
**permissions** | [**List[ApiPermissionGrant]**](ApiPermissionGrant.md) | Explicit scoped or legacy umbrella grants for CUSTOM or an omitted roleType. Required and nonempty when roleType is CUSTOM. For predefined role types, omit this field or supply an empty array. Legacy requests without roleType keep the default grants when this is empty. | [optional] 

## Example

```python
from formkiq_client.models.add_api_key_request import AddApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddApiKeyRequest from a JSON string
add_api_key_request_instance = AddApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(AddApiKeyRequest.to_json())

# convert the object into a dict
add_api_key_request_dict = add_api_key_request_instance.to_dict()
# create an instance of AddApiKeyRequest from a dict
add_api_key_request_from_dict = AddApiKeyRequest.from_dict(add_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


