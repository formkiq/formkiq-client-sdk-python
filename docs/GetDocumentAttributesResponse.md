# GetDocumentAttributesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**attributes** | [**List[DocumentAttribute]**](DocumentAttribute.md) | List of attributes | [optional] 

## Example

```python
from formkiq_client.models.get_document_attributes_response import GetDocumentAttributesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentAttributesResponse from a JSON string
get_document_attributes_response_instance = GetDocumentAttributesResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentAttributesResponse.to_json())

# convert the object into a dict
get_document_attributes_response_dict = get_document_attributes_response_instance.to_dict()
# create an instance of GetDocumentAttributesResponse from a dict
get_document_attributes_response_from_dict = GetDocumentAttributesResponse.from_dict(get_document_attributes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


