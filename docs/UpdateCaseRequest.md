# UpdateCaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case** | [**UpdateCase**](UpdateCase.md) |  | [optional] 

## Example

```python
from formkiq_client.models.update_case_request import UpdateCaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCaseRequest from a JSON string
update_case_request_instance = UpdateCaseRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCaseRequest.to_json())

# convert the object into a dict
update_case_request_dict = update_case_request_instance.to_dict()
# create an instance of UpdateCaseRequest from a dict
update_case_request_from_dict = UpdateCaseRequest.from_dict(update_case_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


