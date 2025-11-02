# GetClassificationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**classifications** | [**List[ClassificationSummary]**](ClassificationSummary.md) | List of classifications | [optional] 

## Example

```python
from openapi_client.model.get_classifications_response import GetClassificationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClassificationsResponse from a JSON string
get_classifications_response_instance = GetClassificationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetClassificationsResponse.to_json())

# convert the object into a dict
get_classifications_response_dict = get_classifications_response_instance.to_dict()
# create an instance of GetClassificationsResponse from a dict
get_classifications_response_from_dict = GetClassificationsResponse.from_dict(get_classifications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


