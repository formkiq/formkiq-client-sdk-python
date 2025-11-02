# AddSite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Site Id | [optional] 
**title** | **str** | Title of Site | [optional] 
**status** | [**SiteStatus**](SiteStatus.md) |  | [optional] 

## Example

```python
from openapi_client.model.add_site import AddSite

# TODO update the JSON string below
json = "{}"
# create an instance of AddSite from a JSON string
add_site_instance = AddSite.from_json(json)
# print the JSON string representation of the object
print(AddSite.to_json())

# convert the object into a dict
add_site_dict = add_site_instance.to_dict()
# create an instance of AddSite from a dict
add_site_from_dict = AddSite.from_dict(add_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


