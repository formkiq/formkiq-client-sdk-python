# AddDocumentCertificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (NEW_VERSION / NEW_DOCUMENT). | [optional] 
**url** | **str** | Presigned download URL (DOWNLOAD). | [optional] 

## Example

```python
from formkiq_client.models.add_document_certification_response import AddDocumentCertificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentCertificationResponse from a JSON string
add_document_certification_response_instance = AddDocumentCertificationResponse.from_json(json)
# print the JSON string representation of the object
print(AddDocumentCertificationResponse.to_json())

# convert the object into a dict
add_document_certification_response_dict = add_document_certification_response_instance.to_dict()
# create an instance of AddDocumentCertificationResponse from a dict
add_document_certification_response_from_dict = AddDocumentCertificationResponse.from_dict(add_document_certification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


