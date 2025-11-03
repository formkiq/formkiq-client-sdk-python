# AddMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Mapping | [optional] 
**description** | **str** | Description of Mapping | [optional] 
**attributes** | [**List[MappingAttribute]**](MappingAttribute.md) | List of attributes | [optional] 

## Example

```python
from formkiq_client.models.add_mapping import AddMapping

# TODO update the JSON string below
json = "{}"
# create an instance of AddMapping from a JSON string
add_mapping_instance = AddMapping.from_json(json)
# print the JSON string representation of the object
print(AddMapping.to_json())

# convert the object into a dict
add_mapping_dict = add_mapping_instance.to_dict()
# create an instance of AddMapping from a dict
add_mapping_from_dict = AddMapping.from_dict(add_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


