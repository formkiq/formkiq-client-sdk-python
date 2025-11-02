# Mapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping_id** | **str** | Mapping Identifier | [optional] 
**name** | **str** | Name of Mapping | [optional] 
**description** | **str** | Description of Mapping | [optional] 
**attributes** | [**List[MappingAttribute]**](MappingAttribute.md) | List of attributes | [optional] 

## Example

```python
from openapi_client.model.mapping import Mapping

# TODO update the JSON string below
json = "{}"
# create an instance of Mapping from a JSON string
mapping_instance = Mapping.from_json(json)
# print the JSON string representation of the object
print(Mapping.to_json())

# convert the object into a dict
mapping_dict = mapping_instance.to_dict()
# create an instance of Mapping from a dict
mapping_from_dict = Mapping.from_dict(mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


