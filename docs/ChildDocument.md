# ChildDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path or Name of document | [optional] 
**width** | **str** | Document Content Width property | [optional] 
**height** | **str** | Document Content Height property | [optional] 
**deep_link_path** | **str** | Path or Name of deep link | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**last_modified_date** | **str** | Last Modified Timestamp | [optional] 
**checksum** | **str** | Document checksum, changes when document file changes | [optional] 
**document_id** | **str** | Document Identifier | 
**content_type** | **str** | Document Content-Type | [optional] 
**user_id** | **str** | User who added document | [optional] 
**content_length** | **int** | Document size | [optional] 
**version_id** | **str** | Document version | [optional] 
**belongs_to_document_id** | **str** | Parent Document Identifier | [optional] 

## Example

```python
from openapi_client.model.child_document import ChildDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ChildDocument from a JSON string
child_document_instance = ChildDocument.from_json(json)
# print the JSON string representation of the object
print(ChildDocument.to_json())

# convert the object into a dict
child_document_dict = child_document_instance.to_dict()
# create an instance of ChildDocument from a dict
child_document_from_dict = ChildDocument.from_dict(child_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


