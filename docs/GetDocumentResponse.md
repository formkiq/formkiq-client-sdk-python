# GetDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **str** | Site Identifier | [optional] 
**path** | **str** | Path or Name of document | [optional] 
**deep_link_path** | **str** | Path or Name of deep link | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**last_modified_date** | **str** | Last Modified Timestamp | [optional] 
**checksum** | **str** | Document checksum, changes when document file changes | [optional] 
**document_id** | **str** | Document Identifier | 
**content_type** | **str** | Document Content-Type | [optional] 
**user_id** | **str** | User who added document | [optional] 
**content_length** | **int** | Document size | [optional] 
**version_id** | **str** | Document version | [optional] 
**documents** | [**List[ChildDocument]**](ChildDocument.md) | List of child documents | [optional] 
**belongs_to_document_id** | **str** | Parent Document Identifier | [optional] 
**metadata** | [**List[DocumentMetadata]**](DocumentMetadata.md) | List of document Metadata | [optional] 

## Example

```python
from formkiq_client.models.get_document_response import GetDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentResponse from a JSON string
get_document_response_instance = GetDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentResponse.to_json())

# convert the object into a dict
get_document_response_dict = get_document_response_instance.to_dict()
# create an instance of GetDocumentResponse from a dict
get_document_response_form_dict = get_document_response.from_dict(get_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


