# SetDocumentDataClassificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Result content | [optional] 
**attributes** | [**List[DataClassificationAttribute]**](DataClassificationAttribute.md) | Attributes extracted from result content | [optional] 

## Example

```python
from formkiq_client.models.set_document_data_classification_response import SetDocumentDataClassificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetDocumentDataClassificationResponse from a JSON string
set_document_data_classification_response_instance = SetDocumentDataClassificationResponse.from_json(json)
# print the JSON string representation of the object
print(SetDocumentDataClassificationResponse.to_json())

# convert the object into a dict
set_document_data_classification_response_dict = set_document_data_classification_response_instance.to_dict()
# create an instance of SetDocumentDataClassificationResponse from a dict
set_document_data_classification_response_from_dict = SetDocumentDataClassificationResponse.from_dict(set_document_data_classification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


