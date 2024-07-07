# AttributeSchemaOptional


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** |  | [optional] 
**allowed_values** | **List[str]** | Only valid string values | [optional] 

## Example

```python
from formkiq_client.models.attribute_schema_optional import AttributeSchemaOptional

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeSchemaOptional from a JSON string
attribute_schema_optional_instance = AttributeSchemaOptional.from_json(json)
# print the JSON string representation of the object
print(AttributeSchemaOptional.to_json())

# convert the object into a dict
attribute_schema_optional_dict = attribute_schema_optional_instance.to_dict()
# create an instance of AttributeSchemaOptional from a dict
attribute_schema_optional_from_dict = AttributeSchemaOptional.from_dict(attribute_schema_optional_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


