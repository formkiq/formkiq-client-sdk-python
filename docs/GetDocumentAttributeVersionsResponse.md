# GetDocumentAttributeVersionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**attributes** | [**List[DocumentAttribute]**](DocumentAttribute.md) | List of document attribute versions | [optional] 

## Example

```python
from formkiq_client.models.get_document_attribute_versions_response import GetDocumentAttributeVersionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentAttributeVersionsResponse from a JSON string
get_document_attribute_versions_response_instance = GetDocumentAttributeVersionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentAttributeVersionsResponse.to_json())

# convert the object into a dict
get_document_attribute_versions_response_dict = get_document_attribute_versions_response_instance.to_dict()
# create an instance of GetDocumentAttributeVersionsResponse from a dict
get_document_attribute_versions_response_from_dict = GetDocumentAttributeVersionsResponse.from_dict(get_document_attribute_versions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


