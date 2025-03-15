# AttributeSchemaRequired


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** |  | [optional] 
**min_number_of_values** | **float** | The minimum number of attribute values | [optional] 
**max_number_of_values** | **float** | The maximum number of attribute values | [optional] 
**default_value** | **str** | Default value | [optional] 
**default_values** | **List[str]** | Default values | [optional] 
**allowed_values** | **List[str]** | Only valid string values | [optional] 
**localized_allowed_values** | **Dict[str, str]** |  | [optional] 

## Example

```python
from formkiq_client.models.attribute_schema_required import AttributeSchemaRequired

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeSchemaRequired from a JSON string
attribute_schema_required_instance = AttributeSchemaRequired.from_json(json)
# print the JSON string representation of the object
print(AttributeSchemaRequired.to_json())

# convert the object into a dict
attribute_schema_required_dict = attribute_schema_required_instance.to_dict()
# create an instance of AttributeSchemaRequired from a dict
attribute_schema_required_from_dict = AttributeSchemaRequired.from_dict(attribute_schema_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


