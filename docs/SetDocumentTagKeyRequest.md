# SetDocumentTagKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Tag value | [optional] 
**values** | **List[str]** | Tag values | [optional] 

## Example

```python
from formkiq_client.models.set_document_tag_key_request import SetDocumentTagKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDocumentTagKeyRequest from a JSON string
set_document_tag_key_request_instance = SetDocumentTagKeyRequest.from_json(json)
# print the JSON string representation of the object
print(SetDocumentTagKeyRequest.to_json())

# convert the object into a dict
set_document_tag_key_request_dict = set_document_tag_key_request_instance.to_dict()
# create an instance of SetDocumentTagKeyRequest from a dict
set_document_tag_key_request_form_dict = set_document_tag_key_request.from_dict(set_document_tag_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


