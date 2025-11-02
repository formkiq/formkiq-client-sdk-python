# DocumentSearchRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | Start of range query | 
**end** | **str** | End of range query | 
**type** | [**SearchRangeDataType**](SearchRangeDataType.md) |  | [optional] [default to SearchRangeDataType.STRING]

## Example

```python
from openapi_client.model.document_search_range import DocumentSearchRange

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchRange from a JSON string
document_search_range_instance = DocumentSearchRange.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchRange.to_json())

# convert the object into a dict
document_search_range_dict = document_search_range_instance.to_dict()
# create an instance of DocumentSearchRange from a dict
document_search_range_from_dict = DocumentSearchRange.from_dict(document_search_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


