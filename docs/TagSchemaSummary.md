# TagSchemaSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_schema_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**in_use** | **bool** | Whether the TagSchema is in use | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 

## Example

```python
from formkiq_client.models.tag_schema_summary import TagSchemaSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TagSchemaSummary from a JSON string
tag_schema_summary_instance = TagSchemaSummary.from_json(json)
# print the JSON string representation of the object
print(TagSchemaSummary.to_json())

# convert the object into a dict
tag_schema_summary_dict = tag_schema_summary_instance.to_dict()
# create an instance of TagSchemaSummary from a dict
tag_schema_summary_from_dict = TagSchemaSummary.from_dict(tag_schema_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


