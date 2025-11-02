# SearchResponseFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **List[str]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.search_response_fields import SearchResponseFields

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseFields from a JSON string
search_response_fields_instance = SearchResponseFields.from_json(json)
# print the JSON string representation of the object
print(SearchResponseFields.to_json())

# convert the object into a dict
search_response_fields_dict = search_response_fields_instance.to_dict()
# create an instance of SearchResponseFields from a dict
search_response_fields_from_dict = SearchResponseFields.from_dict(search_response_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


