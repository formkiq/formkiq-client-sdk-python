# AddClassificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | [**AddClassification**](AddClassification.md) |  | [optional] 

## Example

```python
from openapi_client.models.add_classification_request import AddClassificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddClassificationRequest from a JSON string
add_classification_request_instance = AddClassificationRequest.from_json(json)
# print the JSON string representation of the object
print(AddClassificationRequest.to_json())

# convert the object into a dict
add_classification_request_dict = add_classification_request_instance.to_dict()
# create an instance of AddClassificationRequest from a dict
add_classification_request_from_dict = AddClassificationRequest.from_dict(add_classification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


