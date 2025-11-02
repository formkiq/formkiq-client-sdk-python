# TextractQuery

A question to ask Textract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Natural-language question | [optional] 
**alias** | **str** | Label to identify this query in the result | [optional] 
**pages** | **List[str]** | Page selection | [optional] 

## Example

```python
from openapi_client.models.textract_query import TextractQuery

# TODO update the JSON string below
json = "{}"
# create an instance of TextractQuery from a JSON string
textract_query_instance = TextractQuery.from_json(json)
# print the JSON string representation of the object
print(TextractQuery.to_json())

# convert the object into a dict
textract_query_dict = textract_query_instance.to_dict()
# create an instance of TextractQuery from a dict
textract_query_from_dict = TextractQuery.from_dict(textract_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


