# DocumentFulltextAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | [**DocumentFulltextAttributeEq**](DocumentFulltextAttributeEq.md) |  | [optional] 
**eq_or** | [**List[DocumentFulltextAttributeEq]**](DocumentFulltextAttributeEq.md) | Searches for ANY strings that eq | [optional] 
**key** | **str** | Tag key to search | 

## Example

```python
from openapi_client.model.document_fulltext_attribute import DocumentFulltextAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFulltextAttribute from a JSON string
document_fulltext_attribute_instance = DocumentFulltextAttribute.from_json(json)
# print the JSON string representation of the object
print(DocumentFulltextAttribute.to_json())

# convert the object into a dict
document_fulltext_attribute_dict = document_fulltext_attribute_instance.to_dict()
# create an instance of DocumentFulltextAttribute from a dict
document_fulltext_attribute_from_dict = DocumentFulltextAttribute.from_dict(document_fulltext_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


