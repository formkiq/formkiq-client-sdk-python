# AddReindexDocumentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**ReindexTarget**](ReindexTarget.md) |  | [optional] 

## Example

```python
from openapi_client.models.add_reindex_document_request import AddReindexDocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddReindexDocumentRequest from a JSON string
add_reindex_document_request_instance = AddReindexDocumentRequest.from_json(json)
# print the JSON string representation of the object
print(AddReindexDocumentRequest.to_json())

# convert the object into a dict
add_reindex_document_request_dict = add_reindex_document_request_instance.to_dict()
# create an instance of AddReindexDocumentRequest from a dict
add_reindex_document_request_from_dict = AddReindexDocumentRequest.from_dict(add_reindex_document_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


