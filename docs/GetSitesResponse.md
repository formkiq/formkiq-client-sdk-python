# GetSitesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username of request caller | [optional] 
**roles** | **List[str]** |  | [optional] 
**saml_groups** | **List[str]** | List of User Saml Groups | [optional] 
**user_claims** | **Dict[str, object]** | Custom claims for the authenticated caller, from a JWT or API key. Values retain their JSON types, including strings, numbers, Booleans, arrays, and objects. Null-valued object fields are omitted. | [optional] 
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
get_sites_response_from_dict = GetSitesResponse.from_dict(get_sites_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


