# AddAttributeSchemaOptional


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_number_of_values** | **float** | The minimum number of attribute values | [optional] 
**max_number_of_values** | **float** | The maximum number of attribute values | [optional] 
**attribute_key** | **str** |  | [optional] 
**allowed_values** | **List[str]** | Only valid string values | [optional] 

## Example

```python
from formkiq_client.models.add_attribute_schema_optional import AddAttributeSchemaOptional

# TODO update the JSON string below
json = "{}"
# create an instance of AddAttributeSchemaOptional from a JSON string
add_attribute_schema_optional_instance = AddAttributeSchemaOptional.from_json(json)
# print the JSON string representation of the object
print(AddAttributeSchemaOptional.to_json())

# convert the object into a dict
add_attribute_schema_optional_dict = add_attribute_schema_optional_instance.to_dict()
# create an instance of AddAttributeSchemaOptional from a dict
add_attribute_schema_optional_from_dict = AddAttributeSchemaOptional.from_dict(add_attribute_schema_optional_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


