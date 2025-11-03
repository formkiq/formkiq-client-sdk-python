# ApiKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of API Key | [optional] 
**api_key** | **str** | API Key value | [optional] 
**user_id** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**permissions** | **List[str]** | List of permissions | [optional] 

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


