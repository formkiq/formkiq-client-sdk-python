# DocumentFulltextAttributeEq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_value** | **str** | Search for string value | [optional] 
**number_value** | **float** | Search for number value | [optional] 
**boolean_value** | **bool** | Search for boolean value | [optional] 

## Example

```python
from openapi_client.model.document_fulltext_attribute_eq import DocumentFulltextAttributeEq

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFulltextAttributeEq from a JSON string
document_fulltext_attribute_eq_instance = DocumentFulltextAttributeEq.from_json(json)
# print the JSON string representation of the object
print(DocumentFulltextAttributeEq.to_json())

# convert the object into a dict
document_fulltext_attribute_eq_dict = document_fulltext_attribute_eq_instance.to_dict()
# create an instance of DocumentFulltextAttributeEq from a dict
document_fulltext_attribute_eq_from_dict = DocumentFulltextAttributeEq.from_dict(document_fulltext_attribute_eq_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


