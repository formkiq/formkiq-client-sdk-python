# AddDocumentTag

List of Document Tags (use either 'value' or 'values' not both)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Tag key | 
**value** | **str** | Tag value | [optional] 
**values** | **List[str]** | Tag values | [optional] 

## Example

```python
from formkiq_client.models.add_document_tag import AddDocumentTag

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentTag from a JSON string
add_document_tag_instance = AddDocumentTag.from_json(json)
# print the JSON string representation of the object
print AddDocumentTag.to_json()

# convert the object into a dict
add_document_tag_dict = add_document_tag_instance.to_dict()
# create an instance of AddDocumentTag from a dict
add_document_tag_form_dict = add_document_tag.from_dict(add_document_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


