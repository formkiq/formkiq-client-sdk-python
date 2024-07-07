# SetClassificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | [**AddClassification**](AddClassification.md) |  | [optional] 

## Example

```python
from formkiq_client.models.set_classification_request import SetClassificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetClassificationRequest from a JSON string
set_classification_request_instance = SetClassificationRequest.from_json(json)
# print the JSON string representation of the object
print(SetClassificationRequest.to_json())

# convert the object into a dict
set_classification_request_dict = set_classification_request_instance.to_dict()
# create an instance of SetClassificationRequest from a dict
set_classification_request_from_dict = SetClassificationRequest.from_dict(set_classification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


