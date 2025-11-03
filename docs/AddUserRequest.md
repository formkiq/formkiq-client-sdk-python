# AddUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**AddUser**](AddUser.md) |  | 

## Example

```python
from formkiq_client.models.add_user_request import AddUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserRequest from a JSON string
add_user_request_instance = AddUserRequest.from_json(json)
# print the JSON string representation of the object
print(AddUserRequest.to_json())

# convert the object into a dict
add_user_request_dict = add_user_request_instance.to_dict()
# create an instance of AddUserRequest from a dict
add_user_request_from_dict = AddUserRequest.from_dict(add_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


