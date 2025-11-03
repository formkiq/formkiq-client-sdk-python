# GetEntitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**entities** | [**List[Entity]**](Entity.md) | List of Entities | [optional] 

## Example

```python
from formkiq_client.models.get_entities_response import GetEntitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntitiesResponse from a JSON string
get_entities_response_instance = GetEntitiesResponse.from_json(json)
# print the JSON string representation of the object
print(GetEntitiesResponse.to_json())

# convert the object into a dict
get_entities_response_dict = get_entities_response_instance.to_dict()
# create an instance of GetEntitiesResponse from a dict
get_entities_response_from_dict = GetEntitiesResponse.from_dict(get_entities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


