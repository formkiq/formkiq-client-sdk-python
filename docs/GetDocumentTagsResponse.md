# GetDocumentTagsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**previous** | **str** | Previous page of results token | [optional] 
**tags** | [**List[DocumentTag]**](DocumentTag.md) | List of tags | [optional] 

## Example

```python
from formkiq_client.models.get_document_tags_response import GetDocumentTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentTagsResponse from a JSON string
get_document_tags_response_instance = GetDocumentTagsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentTagsResponse.to_json())

# convert the object into a dict
get_document_tags_response_dict = get_document_tags_response_instance.to_dict()
# create an instance of GetDocumentTagsResponse from a dict
get_document_tags_response_from_dict = GetDocumentTagsResponse.from_dict(get_document_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


