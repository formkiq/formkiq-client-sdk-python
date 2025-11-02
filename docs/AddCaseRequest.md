# AddCaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case** | [**AddCase**](AddCase.md) |  | 

## Example

```python
from openapi_client.models.add_case_request import AddCaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddCaseRequest from a JSON string
add_case_request_instance = AddCaseRequest.from_json(json)
# print the JSON string representation of the object
print(AddCaseRequest.to_json())

# convert the object into a dict
add_case_request_dict = add_case_request_instance.to_dict()
# create an instance of AddCaseRequest from a dict
add_case_request_from_dict = AddCaseRequest.from_dict(add_case_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


