# DocumentFulltextRequest

Document full text search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**DocumentFulltextSearch**](DocumentFulltextSearch.md) |  | 
**response_fields** | [**SearchResponseFields**](SearchResponseFields.md) |  | [optional] 

## Example

```python
from formkiq_client.models.document_fulltext_request import DocumentFulltextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFulltextRequest from a JSON string
document_fulltext_request_instance = DocumentFulltextRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentFulltextRequest.to_json())

# convert the object into a dict
document_fulltext_request_dict = document_fulltext_request_instance.to_dict()
# create an instance of DocumentFulltextRequest from a dict
document_fulltext_request_form_dict = document_fulltext_request.from_dict(document_fulltext_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


