# AddTagSchemaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_schema_id** | **str** | Tag Schema Identifier | [optional] 

## Example

```python
from formkiq_client.models.add_tag_schema_response import AddTagSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddTagSchemaResponse from a JSON string
add_tag_schema_response_instance = AddTagSchemaResponse.from_json(json)
# print the JSON string representation of the object
print(AddTagSchemaResponse.to_json())

# convert the object into a dict
add_tag_schema_response_dict = add_tag_schema_response_instance.to_dict()
# create an instance of AddTagSchemaResponse from a dict
add_tag_schema_response_from_dict = AddTagSchemaResponse.from_dict(add_tag_schema_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


