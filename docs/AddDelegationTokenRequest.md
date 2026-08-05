# AddDelegationTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[DelegationTokenPermission]**](DelegationTokenPermission.md) | Permissions to keep while the delegation token is applied. These must be a subset of the caller&#39;s current permissions for the site and cannot include ADMIN. | 
**on_behalf_of** | [**DelegationTokenPrincipal**](DelegationTokenPrincipal.md) |  | [optional] 
**reason** | **str** | Reason the delegation token is being generated. Stored in the signed token for audit/support traceability. | 

## Example

```python
from formkiq_client.models.add_delegation_token_request import AddDelegationTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDelegationTokenRequest from a JSON string
add_delegation_token_request_instance = AddDelegationTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AddDelegationTokenRequest.to_json())

# convert the object into a dict
add_delegation_token_request_dict = add_delegation_token_request_instance.to_dict()
# create an instance of AddDelegationTokenRequest from a dict
add_delegation_token_request_from_dict = AddDelegationTokenRequest.from_dict(add_delegation_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


