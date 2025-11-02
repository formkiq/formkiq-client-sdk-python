# AddShare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | Share with Group | [optional] 
**permissions** | [**List[UserSharePermission]**](UserSharePermission.md) | List of share permissions | [optional] 

## Example

```python
from openapi_client.models.add_share import AddShare

# TODO update the JSON string below
json = "{}"
# create an instance of AddShare from a JSON string
add_share_instance = AddShare.from_json(json)
# print the JSON string representation of the object
print(AddShare.to_json())

# convert the object into a dict
add_share_dict = add_share_instance.to_dict()
# create an instance of AddShare from a dict
add_share_from_dict = AddShare.from_dict(add_share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


