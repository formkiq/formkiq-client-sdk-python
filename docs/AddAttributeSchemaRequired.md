# AddAttributeSchemaRequired


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_number_of_values** | **float** | The minimum number of attribute values | [optional] 
**max_number_of_values** | **float** | The maximum number of attribute values | [optional] 
**attribute_key** | **str** |  | [optional] 
**default_value** | **str** | Default value | [optional] 
**default_values** | **List[str]** | Default values | [optional] 
**allowed_values** | **List[str]** | Only valid string values | [optional] 

## Example

```python
from openapi_client.models.add_attribute_schema_required import AddAttributeSchemaRequired

# TODO update the JSON string below
json = "{}"
# create an instance of AddAttributeSchemaRequired from a JSON string
add_attribute_schema_required_instance = AddAttributeSchemaRequired.from_json(json)
# print the JSON string representation of the object
print(AddAttributeSchemaRequired.to_json())

# convert the object into a dict
add_attribute_schema_required_dict = add_attribute_schema_required_instance.to_dict()
# create an instance of AddAttributeSchemaRequired from a dict
add_attribute_schema_required_from_dict = AddAttributeSchemaRequired.from_dict(add_attribute_schema_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


