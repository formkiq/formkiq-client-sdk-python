# SearchResultDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **str** | Site Identifier | [optional] 
**path** | **str** | Path or Name of document | [optional] 
**deep_link_path** | **str** | Path or Name of deep link | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**last_modified_date** | **str** | Last Modified Timestamp | [optional] 
**folder** | **bool** | Is Result a Document Folder | [optional] 
**index_key** | **str** | populated if search result are from an index | [optional] 
**checksum** | **str** | Document checksum, changes when document file changes | [optional] 
**checksum_type** | [**ChecksumType**](ChecksumType.md) |  | [optional] 
**document_id** | **str** | Document Identifier | [optional] 
**content_type** | **str** | Document Content-Type | [optional] 
**user_id** | **str** | User who added document | [optional] 
**content_length** | **int** | Document size | [optional] 
**version_id** | **str** | Document version | [optional] 
**belongs_to_document_id** | **str** | Parent Document Identifier | [optional] 
**matched_attribute** | [**DocumentSearchMatchAttribute**](DocumentSearchMatchAttribute.md) |  | [optional] 
**matched_tag** | [**DocumentSearchMatchTag**](DocumentSearchMatchTag.md) |  | [optional] 
**matched_tags** | [**List[DocumentSearchMatchTag]**](DocumentSearchMatchTag.md) |  | [optional] 
**tags** | **Dict[str, object]** |  | [optional] 
**attributes** | [**Dict[str, SearchResultDocumentAttribute]**](SearchResultDocumentAttribute.md) |  | [optional] 
**metadata** | [**List[DocumentMetadata]**](DocumentMetadata.md) | List of document Metadata | [optional] 

## Example

```python
from formkiq_client.models.search_result_document import SearchResultDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultDocument from a JSON string
search_result_document_instance = SearchResultDocument.from_json(json)
# print the JSON string representation of the object
print(SearchResultDocument.to_json())

# convert the object into a dict
search_result_document_dict = search_result_document_instance.to_dict()
# create an instance of SearchResultDocument from a dict
search_result_document_from_dict = SearchResultDocument.from_dict(search_result_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


