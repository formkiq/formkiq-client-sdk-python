# UpdateCaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_id** | **str** | Case Identifier | [optional] 

## Example

```python
from formkiq_client.models.update_case_response import UpdateCaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCaseResponse from a JSON string
update_case_response_instance = UpdateCaseResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCaseResponse.to_json())

# convert the object into a dict
update_case_response_dict = update_case_response_instance.to_dict()
# create an instance of UpdateCaseResponse from a dict
update_case_response_form_dict = update_case_response.from_dict(update_case_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


