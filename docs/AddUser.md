# AddUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Email address of user | [optional] 

## Example

```python
from formkiq_client.models.add_user import AddUser

# TODO update the JSON string below
json = "{}"
# create an instance of AddUser from a JSON string
add_user_instance = AddUser.from_json(json)
# print the JSON string representation of the object
print(AddUser.to_json())

# convert the object into a dict
add_user_dict = add_user_instance.to_dict()
# create an instance of AddUser from a dict
add_user_from_dict = AddUser.from_dict(add_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


