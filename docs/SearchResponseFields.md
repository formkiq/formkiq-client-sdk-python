# SearchResponseFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 

## Example

```python
from formkiq_client.models.search_response_fields import SearchResponseFields

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseFields from a JSON string
search_response_fields_instance = SearchResponseFields.from_json(json)
# print the JSON string representation of the object
print SearchResponseFields.to_json()

# convert the object into a dict
search_response_fields_dict = search_response_fields_instance.to_dict()
# create an instance of SearchResponseFields from a dict
search_response_fields_form_dict = search_response_fields.from_dict(search_response_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


