# GetDocumentMetadataExtractionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**metadata_extractions** | [**List[MetadataExtraction]**](MetadataExtraction.md) | List of Metadata Extractions | [optional] 

## Example

```python
from formkiq_client.models.get_document_metadata_extraction_response import GetDocumentMetadataExtractionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentMetadataExtractionResponse from a JSON string
get_document_metadata_extraction_response_instance = GetDocumentMetadataExtractionResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentMetadataExtractionResponse.to_json())

# convert the object into a dict
get_document_metadata_extraction_response_dict = get_document_metadata_extraction_response_instance.to_dict()
# create an instance of GetDocumentMetadataExtractionResponse from a dict
get_document_metadata_extraction_response_from_dict = GetDocumentMetadataExtractionResponse.from_dict(get_document_metadata_extraction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


