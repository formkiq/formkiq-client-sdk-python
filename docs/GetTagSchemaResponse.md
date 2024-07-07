# GetTagSchemaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_schema** | [**TagSchema**](TagSchema.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_tag_schema_response import GetTagSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagSchemaResponse from a JSON string
get_tag_schema_response_instance = GetTagSchemaResponse.from_json(json)
# print the JSON string representation of the object
print(GetTagSchemaResponse.to_json())

# convert the object into a dict
get_tag_schema_response_dict = get_tag_schema_response_instance.to_dict()
# create an instance of GetTagSchemaResponse from a dict
get_tag_schema_response_from_dict = GetTagSchemaResponse.from_dict(get_tag_schema_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


