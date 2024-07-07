# DocumentMetadata

Document Metadata (use either 'value' or 'values' not both)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Metadata key | [optional] 
**value** | **str** | Metadata value | [optional] 
**values** | **List[str]** | Metadata values | [optional] 

## Example

```python
from formkiq_client.models.document_metadata import DocumentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentMetadata from a JSON string
document_metadata_instance = DocumentMetadata.from_json(json)
# print the JSON string representation of the object
print(DocumentMetadata.to_json())

# convert the object into a dict
document_metadata_dict = document_metadata_instance.to_dict()
# create an instance of DocumentMetadata from a dict
document_metadata_from_dict = DocumentMetadata.from_dict(document_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


