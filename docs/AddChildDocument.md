# AddChildDocument

List of related documents

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path or Name of document | [optional] 
**width** | **str** | Document Content Width property | [optional] 
**height** | **str** | Document Content Height property | [optional] 
**deep_link_path** | **str** | Path or Name of deep link | [optional] 
**content_type** | **str** | Document Content-Type | [optional] 
**checksum_type** | [**ChecksumType**](ChecksumType.md) |  | [optional] 
**checksum** | **str** | The checksum value to validate the file against | [optional] 
**is_base64** | **bool** | Is the content Base64-encoded? | [optional] 
**content** | **str** | Document content | 
**tags** | [**List[AddDocumentTag]**](AddDocumentTag.md) | List of document tags | [optional] 
**metadata** | [**List[AddDocumentMetadata]**](AddDocumentMetadata.md) | List of document Metadata | [optional] 

## Example

```python
from openapi_client.models.add_child_document import AddChildDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AddChildDocument from a JSON string
add_child_document_instance = AddChildDocument.from_json(json)
# print the JSON string representation of the object
print(AddChildDocument.to_json())

# convert the object into a dict
add_child_document_dict = add_child_document_instance.to_dict()
# create an instance of AddChildDocument from a dict
add_child_document_from_dict = AddChildDocument.from_dict(add_child_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


