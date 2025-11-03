# AddDocumentMetadata

Document Metadata (use either 'value' or 'values' not both)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Metadata key | 
**value** | **str** | Metadata value | [optional] 
**values** | **List[str]** | Metadata values | [optional] 

## Example

```python
from formkiq_client.models.add_document_metadata import AddDocumentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentMetadata from a JSON string
add_document_metadata_instance = AddDocumentMetadata.from_json(json)
# print the JSON string representation of the object
print(AddDocumentMetadata.to_json())

# convert the object into a dict
add_document_metadata_dict = add_document_metadata_instance.to_dict()
# create an instance of AddDocumentMetadata from a dict
add_document_metadata_from_dict = AddDocumentMetadata.from_dict(add_document_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


