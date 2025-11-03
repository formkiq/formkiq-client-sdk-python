# GetSitesSchemaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of schema | [optional] 
**attributes** | [**SchemaAttributes**](SchemaAttributes.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_sites_schema_response import GetSitesSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSitesSchemaResponse from a JSON string
get_sites_schema_response_instance = GetSitesSchemaResponse.from_json(json)
# print the JSON string representation of the object
print(GetSitesSchemaResponse.to_json())

# convert the object into a dict
get_sites_schema_response_dict = get_sites_schema_response_instance.to_dict()
# create an instance of GetSitesSchemaResponse from a dict
get_sites_schema_response_from_dict = GetSitesSchemaResponse.from_dict(get_sites_schema_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


