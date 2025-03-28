# GetDocumentFulltextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **str** | Site Identifier | [optional] 
**content** | **str** | Content of document | [optional] 
**content_type** | **str** | Document Content-Type | [optional] 
**path** | **str** | Path or Name of document | [optional] 
**width** | **str** | Document Content Width property | [optional] 
**height** | **str** | Document Content Height property | [optional] 
**deep_link_path** | **str** | Path or Name of deep link | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**last_modified_date** | **str** | Last Modified Timestamp | [optional] 
**document_id** | **str** | Document Identifier | [optional] 
**created_by** | **str** | User who added document | [optional] 
**content_length** | **int** | Document size | [optional] 
**checksum** | **str** | Document checksum, changes when document file changes | [optional] 
**checksum_type** | [**ChecksumType**](ChecksumType.md) |  | [optional] 
**tags** | **Dict[str, object]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**attributes** | [**Dict[str, FulltextAttribute]**](FulltextAttribute.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_document_fulltext_response import GetDocumentFulltextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentFulltextResponse from a JSON string
get_document_fulltext_response_instance = GetDocumentFulltextResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentFulltextResponse.to_json())

# convert the object into a dict
get_document_fulltext_response_dict = get_document_fulltext_response_instance.to_dict()
# create an instance of GetDocumentFulltextResponse from a dict
get_document_fulltext_response_from_dict = GetDocumentFulltextResponse.from_dict(get_document_fulltext_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


