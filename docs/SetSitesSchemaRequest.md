# SetSitesSchemaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of schema | [optional] 
**attributes** | [**SetSchemaAttributes**](SetSchemaAttributes.md) |  | [optional] 

## Example

```python
from formkiq_client.models.set_sites_schema_request import SetSitesSchemaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetSitesSchemaRequest from a JSON string
set_sites_schema_request_instance = SetSitesSchemaRequest.from_json(json)
# print the JSON string representation of the object
print(SetSitesSchemaRequest.to_json())

# convert the object into a dict
set_sites_schema_request_dict = set_sites_schema_request_instance.to_dict()
# create an instance of SetSitesSchemaRequest from a dict
set_sites_schema_request_from_dict = SetSitesSchemaRequest.from_dict(set_sites_schema_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


