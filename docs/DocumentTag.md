# DocumentTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**document_id** | **str** | Document Identifier | [optional] 
**type** | **str** | Tag type | [optional] 
**user_id** | **str** | User who added document | [optional] 
**value** | **str** | Tag value | [optional] 
**values** | **List[str]** | Tag values | [optional] 
**key** | **str** | Tag key | [optional] 

## Example

```python
from openapi_client.models.document_tag import DocumentTag

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTag from a JSON string
document_tag_instance = DocumentTag.from_json(json)
# print the JSON string representation of the object
print(DocumentTag.to_json())

# convert the object into a dict
document_tag_dict = document_tag_instance.to_dict()
# create an instance of DocumentTag from a dict
document_tag_from_dict = DocumentTag.from_dict(document_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


