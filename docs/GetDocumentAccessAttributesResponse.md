# GetDocumentAccessAttributesResponse

List of document access attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_attributes** | [**List[AccessAttribute]**](AccessAttribute.md) | List of document access attributes | [optional] 

## Example

```python
from formkiq_client.models.get_document_access_attributes_response import GetDocumentAccessAttributesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentAccessAttributesResponse from a JSON string
get_document_access_attributes_response_instance = GetDocumentAccessAttributesResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentAccessAttributesResponse.to_json())

# convert the object into a dict
get_document_access_attributes_response_dict = get_document_access_attributes_response_instance.to_dict()
# create an instance of GetDocumentAccessAttributesResponse from a dict
get_document_access_attributes_response_form_dict = get_document_access_attributes_response.from_dict(get_document_access_attributes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


