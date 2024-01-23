# AddTagSchemaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**tags** | [**AddTagSchemaTags**](AddTagSchemaTags.md) |  | [optional] 

## Example

```python
from formkiq_client.models.add_tag_schema_request import AddTagSchemaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTagSchemaRequest from a JSON string
add_tag_schema_request_instance = AddTagSchemaRequest.from_json(json)
# print the JSON string representation of the object
print AddTagSchemaRequest.to_json()

# convert the object into a dict
add_tag_schema_request_dict = add_tag_schema_request_instance.to_dict()
# create an instance of AddTagSchemaRequest from a dict
add_tag_schema_request_form_dict = add_tag_schema_request.from_dict(add_tag_schema_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


