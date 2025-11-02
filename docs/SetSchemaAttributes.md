# SetSchemaAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**composite_keys** | [**List[AttributeSchemaCompositeKey]**](AttributeSchemaCompositeKey.md) | List of Composite Keys | [optional] 
**required** | [**List[AddAttributeSchemaRequired]**](AddAttributeSchemaRequired.md) | List of Required Attributes | [optional] 
**optional** | [**List[AddAttributeSchemaOptional]**](AddAttributeSchemaOptional.md) | List of Optional Attribute | [optional] 
**allow_additional_attributes** | **bool** |  | [optional] [default to True]

## Example

```python
from openapi_client.model.set_schema_attributes import SetSchemaAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SetSchemaAttributes from a JSON string
set_schema_attributes_instance = SetSchemaAttributes.from_json(json)
# print the JSON string representation of the object
print(SetSchemaAttributes.to_json())

# convert the object into a dict
set_schema_attributes_dict = set_schema_attributes_instance.to_dict()
# create an instance of SetSchemaAttributes from a dict
set_schema_attributes_from_dict = SetSchemaAttributes.from_dict(set_schema_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


