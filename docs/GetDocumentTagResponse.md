# GetDocumentTagResponse


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
from formkiq_client.models.get_document_tag_response import GetDocumentTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentTagResponse from a JSON string
get_document_tag_response_instance = GetDocumentTagResponse.from_json(json)
# print the JSON string representation of the object
print GetDocumentTagResponse.to_json()

# convert the object into a dict
get_document_tag_response_dict = get_document_tag_response_instance.to_dict()
# create an instance of GetDocumentTagResponse from a dict
get_document_tag_response_form_dict = get_document_tag_response.from_dict(get_document_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


