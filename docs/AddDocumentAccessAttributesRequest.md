# AddDocumentAccessAttributesRequest

List of document access attributes to add

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_attributes** | [**List[AddAccessAttribute]**](AddAccessAttribute.md) | List of document access attributes | [optional] 

## Example

```python
from formkiq_client.models.add_document_access_attributes_request import AddDocumentAccessAttributesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentAccessAttributesRequest from a JSON string
add_document_access_attributes_request_instance = AddDocumentAccessAttributesRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentAccessAttributesRequest.to_json())

# convert the object into a dict
add_document_access_attributes_request_dict = add_document_access_attributes_request_instance.to_dict()
# create an instance of AddDocumentAccessAttributesRequest from a dict
add_document_access_attributes_request_form_dict = add_document_access_attributes_request.from_dict(add_document_access_attributes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


