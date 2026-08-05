# AddDocumentMetadataExtractionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Result content | [optional] 
**attributes** | [**List[DataClassificationAttribute]**](DataClassificationAttribute.md) | Attributes extracted from result content | [optional] 

## Example

```python
from formkiq_client.models.add_document_metadata_extraction_response import AddDocumentMetadataExtractionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentMetadataExtractionResponse from a JSON string
add_document_metadata_extraction_response_instance = AddDocumentMetadataExtractionResponse.from_json(json)
# print the JSON string representation of the object
print(AddDocumentMetadataExtractionResponse.to_json())

# convert the object into a dict
add_document_metadata_extraction_response_dict = add_document_metadata_extraction_response_instance.to_dict()
# create an instance of AddDocumentMetadataExtractionResponse from a dict
add_document_metadata_extraction_response_from_dict = AddDocumentMetadataExtractionResponse.from_dict(add_document_metadata_extraction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


