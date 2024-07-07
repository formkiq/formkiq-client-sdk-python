# Document


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **str** | Site Identifier | [optional] 
**path** | **str** | Path or Name of document | [optional] 
**deep_link_path** | **str** | Path or Name of deep link | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**last_modified_date** | **str** | Last Modified Timestamp | [optional] 
**checksum** | **str** | Document checksum, changes when document file changes | [optional] 
**document_id** | **str** | Document Identifier | [optional] 
**content_type** | **str** | Document Content-Type | [optional] 
**user_id** | **str** | User who added document | [optional] 
**content_length** | **int** | Document size | [optional] 
**version** | **str** | Document version | [optional] 
**version_key** | **str** | Document Version Identifier | [optional] 
**s3version** | **str** | Document storage version | [optional] 
**belongs_to_document_id** | **str** | Parent Document Identifier | [optional] 
**metadata** | [**List[DocumentMetadata]**](DocumentMetadata.md) | List of document Metadata | [optional] 

## Example

```python
from formkiq_client.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


