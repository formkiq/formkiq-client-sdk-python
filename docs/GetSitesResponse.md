# GetSitesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username of request caller | [optional] 
**sites** | [**List[Site]**](Site.md) | List of sites | [optional] 

## Example

```python
from formkiq_client.models.get_sites_response import GetSitesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSitesResponse from a JSON string
get_sites_response_instance = GetSitesResponse.from_json(json)
# print the JSON string representation of the object
print(GetSitesResponse.to_json())

# convert the object into a dict
get_sites_response_dict = get_sites_response_instance.to_dict()
# create an instance of GetSitesResponse from a dict
get_sites_response_form_dict = get_sites_response.from_dict(get_sites_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


