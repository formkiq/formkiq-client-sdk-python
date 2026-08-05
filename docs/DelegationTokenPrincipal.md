# DelegationTokenPrincipal

User identity to store in the signed delegation token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username to use for activity/audit attribution when the delegation token is applied. | 

## Example

```python
from formkiq_client.models.delegation_token_principal import DelegationTokenPrincipal

# TODO update the JSON string below
json = "{}"
# create an instance of DelegationTokenPrincipal from a JSON string
delegation_token_principal_instance = DelegationTokenPrincipal.from_json(json)
# print the JSON string representation of the object
print(DelegationTokenPrincipal.to_json())

# convert the object into a dict
delegation_token_principal_dict = delegation_token_principal_instance.to_dict()
# create an instance of DelegationTokenPrincipal from a dict
delegation_token_principal_from_dict = DelegationTokenPrincipal.from_dict(delegation_token_principal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


