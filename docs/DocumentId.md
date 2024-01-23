# DocumentId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document Identifier | 
**site_id** | **str** | Site Identifier | [optional] 

## Example

```python
from formkiq_client.models.document_id import DocumentId

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentId from a JSON string
document_id_instance = DocumentId.from_json(json)
# print the JSON string representation of the object
print DocumentId.to_json()

# convert the object into a dict
document_id_dict = document_id_instance.to_dict()
# create an instance of DocumentId from a dict
document_id_form_dict = document_id.from_dict(document_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


