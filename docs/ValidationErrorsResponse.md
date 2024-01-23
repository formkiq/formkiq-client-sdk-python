# ValidationErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ValidationError]**](ValidationError.md) | List of errors | [optional] 

## Example

```python
from formkiq_client.models.validation_errors_response import ValidationErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorsResponse from a JSON string
validation_errors_response_instance = ValidationErrorsResponse.from_json(json)
# print the JSON string representation of the object
print ValidationErrorsResponse.to_json()

# convert the object into a dict
validation_errors_response_dict = validation_errors_response_instance.to_dict()
# create an instance of ValidationErrorsResponse from a dict
validation_errors_response_form_dict = validation_errors_response.from_dict(validation_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


