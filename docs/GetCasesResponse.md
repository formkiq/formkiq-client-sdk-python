# GetCasesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**cases** | [**List[Case]**](Case.md) | List of cases | [optional] 

## Example

```python
from formkiq_client.models.get_cases_response import GetCasesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCasesResponse from a JSON string
get_cases_response_instance = GetCasesResponse.from_json(json)
# print the JSON string representation of the object
print(GetCasesResponse.to_json())

# convert the object into a dict
get_cases_response_dict = get_cases_response_instance.to_dict()
# create an instance of GetCasesResponse from a dict
get_cases_response_from_dict = GetCasesResponse.from_dict(get_cases_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


