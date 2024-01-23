# FulltextSearchItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **str** | Site Identifier | [optional] 
**path** | **str** | Path or Name of document | [optional] 
**deep_link_path** | **str** | Path or Name of deep link | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**last_modified_date** | **str** | Last Modified Timestamp | [optional] 
**document_id** | **str** | Document Identifier | [optional] 
**content_length** | **int** | Document size | [optional] 
**created_by** | **str** | User who added document | [optional] 
**tags** | **Dict[str, object]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from formkiq_client.models.fulltext_search_item import FulltextSearchItem

# TODO update the JSON string below
json = "{}"
# create an instance of FulltextSearchItem from a JSON string
fulltext_search_item_instance = FulltextSearchItem.from_json(json)
# print the JSON string representation of the object
print FulltextSearchItem.to_json()

# convert the object into a dict
fulltext_search_item_dict = fulltext_search_item_instance.to_dict()
# create an instance of FulltextSearchItem from a dict
fulltext_search_item_form_dict = fulltext_search_item.from_dict(fulltext_search_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


