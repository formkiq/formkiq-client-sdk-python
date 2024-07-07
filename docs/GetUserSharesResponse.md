# GetUserSharesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**shares** | [**List[UserShare]**](UserShare.md) | List of user&#39;s shares | [optional] 

## Example

```python
from formkiq_client.models.get_user_shares_response import GetUserSharesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserSharesResponse from a JSON string
get_user_shares_response_instance = GetUserSharesResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserSharesResponse.to_json())

# convert the object into a dict
get_user_shares_response_dict = get_user_shares_response_instance.to_dict()
# create an instance of GetUserSharesResponse from a dict
get_user_shares_response_from_dict = GetUserSharesResponse.from_dict(get_user_shares_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


