# SchemaAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**composite_keys** | [**List[AttributeSchemaCompositeKey]**](AttributeSchemaCompositeKey.md) | List of Composite Keys | [optional] 
**required** | [**List[AttributeSchemaRequired]**](AttributeSchemaRequired.md) | List of Required Attributes | [optional] 
**optional** | [**List[AttributeSchemaOptional]**](AttributeSchemaOptional.md) | List of Optional Attribute | [optional] 
**allow_additional_attributes** | **bool** |  | [optional] [default to True]

## Example

```python
from openapi_client.models.schema_attributes import SchemaAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAttributes from a JSON string
schema_attributes_instance = SchemaAttributes.from_json(json)
# print the JSON string representation of the object
print(SchemaAttributes.to_json())

# convert the object into a dict
schema_attributes_dict = schema_attributes_instance.to_dict()
# create an instance of SchemaAttributes from a dict
schema_attributes_from_dict = SchemaAttributes.from_dict(schema_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


