# TagSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_schema_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**tags** | [**TagSchemaTags**](TagSchemaTags.md) |  | [optional] 

## Example

```python
from formkiq_client.models.tag_schema import TagSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TagSchema from a JSON string
tag_schema_instance = TagSchema.from_json(json)
# print the JSON string representation of the object
print TagSchema.to_json()

# convert the object into a dict
tag_schema_dict = tag_schema_instance.to_dict()
# create an instance of TagSchema from a dict
tag_schema_form_dict = tag_schema.from_dict(tag_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


