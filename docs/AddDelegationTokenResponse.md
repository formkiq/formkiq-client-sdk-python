# AddDelegationTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_name** | **str** |  | [optional] 
**delegation_token** | **str** | Signed token to send in the x-formkiq-delegation-token request header. | [optional] 

## Example

```python
from formkiq_client.models.add_delegation_token_response import AddDelegationTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDelegationTokenResponse from a JSON string
add_delegation_token_response_instance = AddDelegationTokenResponse.from_json(json)
# print the JSON string representation of the object
print(AddDelegationTokenResponse.to_json())

# convert the object into a dict
add_delegation_token_response_dict = add_delegation_token_response_instance.to_dict()
# create an instance of AddDelegationTokenResponse from a dict
add_delegation_token_response_from_dict = AddDelegationTokenResponse.from_dict(add_delegation_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


