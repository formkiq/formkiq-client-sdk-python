# GetTagSchemasResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | [**List[TagSchemaSummary]**](TagSchemaSummary.md) | List of Tag Schemas | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 

## Example

```python
from formkiq_client.models.get_tag_schemas_response import GetTagSchemasResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagSchemasResponse from a JSON string
get_tag_schemas_response_instance = GetTagSchemasResponse.from_json(json)
# print the JSON string representation of the object
print(GetTagSchemasResponse.to_json())

# convert the object into a dict
get_tag_schemas_response_dict = get_tag_schemas_response_instance.to_dict()
# create an instance of GetTagSchemasResponse from a dict
get_tag_schemas_response_form_dict = get_tag_schemas_response.from_dict(get_tag_schemas_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


