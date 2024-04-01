# DocumentSearchRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | Start of range query | 
**end** | **str** | End of range query | 

## Example

```python
from formkiq_client.models.document_search_range import DocumentSearchRange

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchRange from a JSON string
document_search_range_instance = DocumentSearchRange.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchRange.to_json())

# convert the object into a dict
document_search_range_dict = document_search_range_instance.to_dict()
# create an instance of DocumentSearchRange from a dict
document_search_range_form_dict = document_search_range.from_dict(document_search_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


