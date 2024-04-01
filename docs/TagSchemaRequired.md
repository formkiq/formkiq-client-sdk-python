# TagSchemaRequired


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**default_values** | **List[str]** | Default values | [optional] 
**allowed_values** | **List[str]** | Only valid values | [optional] 

## Example

```python
from formkiq_client.models.tag_schema_required import TagSchemaRequired

# TODO update the JSON string below
json = "{}"
# create an instance of TagSchemaRequired from a JSON string
tag_schema_required_instance = TagSchemaRequired.from_json(json)
# print the JSON string representation of the object
print(TagSchemaRequired.to_json())

# convert the object into a dict
tag_schema_required_dict = tag_schema_required_instance.to_dict()
# create an instance of TagSchemaRequired from a dict
tag_schema_required_form_dict = tag_schema_required.from_dict(tag_schema_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


