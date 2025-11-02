# GetClassificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | [**Classification**](Classification.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_classification_response import GetClassificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClassificationResponse from a JSON string
get_classification_response_instance = GetClassificationResponse.from_json(json)
# print the JSON string representation of the object
print(GetClassificationResponse.to_json())

# convert the object into a dict
get_classification_response_dict = get_classification_response_instance.to_dict()
# create an instance of GetClassificationResponse from a dict
get_classification_response_from_dict = GetClassificationResponse.from_dict(get_classification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


