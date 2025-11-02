# GetDocumentDataClassificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**data_classifications** | [**List[DataClassification]**](DataClassification.md) | List of Data Classifications | [optional] 

## Example

```python
from formkiq_client.models.get_document_data_classification_response import GetDocumentDataClassificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentDataClassificationResponse from a JSON string
get_document_data_classification_response_instance = GetDocumentDataClassificationResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentDataClassificationResponse.to_json())

# convert the object into a dict
get_document_data_classification_response_dict = get_document_data_classification_response_instance.to_dict()
# create an instance of GetDocumentDataClassificationResponse from a dict
get_document_data_classification_response_from_dict = GetDocumentDataClassificationResponse.from_dict(get_document_data_classification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


