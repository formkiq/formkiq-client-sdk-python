# GetCaseNigosResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**nigos** | [**List[Nigo]**](Nigo.md) | List of Nigos | [optional] 

## Example

```python
from formkiq_client.models.get_case_nigos_response import GetCaseNigosResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCaseNigosResponse from a JSON string
get_case_nigos_response_instance = GetCaseNigosResponse.from_json(json)
# print the JSON string representation of the object
print(GetCaseNigosResponse.to_json())

# convert the object into a dict
get_case_nigos_response_dict = get_case_nigos_response_instance.to_dict()
# create an instance of GetCaseNigosResponse from a dict
get_case_nigos_response_from_dict = GetCaseNigosResponse.from_dict(get_case_nigos_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


