# AddApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of API Key | [optional] 
**permissions** | **List[str]** | List of permissions | [optional] 

## Example

```python
from openapi_client.model.add_api_key_request import AddApiKeyRequest

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


