# DocumentVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**checksum** | **str** | Document checksum, changes when document file changes | [optional] 
**checksum_type** | [**ChecksumType**](ChecksumType.md) |  | [optional] 
**content_type** | **str** | Document Content-Type | [optional] 
**user_id** | **str** | User who added document | [optional] 
**content_length** | **int** | Document size | [optional] 
**version_key** | **str** | Document Version Identifier | [optional] 
**s3version** | **str** | Document storage version | [optional] 

## Example

```python
from formkiq_client.models.document_version import DocumentVersion

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentVersion from a JSON string
document_version_instance = DocumentVersion.from_json(json)
# print the JSON string representation of the object
print(DocumentVersion.to_json())

# convert the object into a dict
document_version_dict = document_version_instance.to_dict()
# create an instance of DocumentVersion from a dict
document_version_from_dict = DocumentVersion.from_dict(document_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


