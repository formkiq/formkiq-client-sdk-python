# AddTagSchemaTags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**composite_keys** | [**List[TagSchemaCompositeKey]**](TagSchemaCompositeKey.md) | List of Composite Keys | [optional] 
**required** | [**List[TagSchemaRequired]**](TagSchemaRequired.md) | List of Required Tags | [optional] 
**optional** | [**List[TagSchemaOptional]**](TagSchemaOptional.md) | List of Optional Tags | [optional] 
**allow_additional_tags** | **bool** |  | [optional] [default to True]

## Example

```python
from formkiq_client.models.add_tag_schema_tags import AddTagSchemaTags

# TODO update the JSON string below
json = "{}"
# create an instance of AddTagSchemaTags from a JSON string
add_tag_schema_tags_instance = AddTagSchemaTags.from_json(json)
# print the JSON string representation of the object
print(AddTagSchemaTags.to_json())

# convert the object into a dict
add_tag_schema_tags_dict = add_tag_schema_tags_instance.to_dict()
# create an instance of AddTagSchemaTags from a dict
add_tag_schema_tags_form_dict = add_tag_schema_tags.from_dict(add_tag_schema_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


