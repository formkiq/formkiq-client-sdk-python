# AddDocumentCertificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**DocumentCertificationTarget**](DocumentCertificationTarget.md) |  | 
**certificates** | [**List[DocumentCertification]**](DocumentCertification.md) | One or more certificates used to certify/sign the document (in order). | 

## Example

```python
from formkiq_client.models.add_document_certification_request import AddDocumentCertificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentCertificationRequest from a JSON string
add_document_certification_request_instance = AddDocumentCertificationRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentCertificationRequest.to_json())

# convert the object into a dict
add_document_certification_request_dict = add_document_certification_request_instance.to_dict()
# create an instance of AddDocumentCertificationRequest from a dict
add_document_certification_request_from_dict = AddDocumentCertificationRequest.from_dict(add_document_certification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


