# GetAttributesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**attributes** | [**List[Attribute]**](Attribute.md) | List of attributes | [optional] 

## Example

```python
from openapi_client.models.get_attributes_response import GetAttributesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAttributesResponse from a JSON string
get_attributes_response_instance = GetAttributesResponse.from_json(json)
# print the JSON string representation of the object
print(GetAttributesResponse.to_json())

# convert the object into a dict
get_attributes_response_dict = get_attributes_response_instance.to_dict()
# create an instance of GetAttributesResponse from a dict
get_attributes_response_from_dict = GetAttributesResponse.from_dict(get_attributes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


