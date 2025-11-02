# UpdateSite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of Site | [optional] 
**status** | [**SiteStatus**](SiteStatus.md) |  | [optional] 

## Example

```python
from openapi_client.model.update_site import UpdateSite

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSite from a JSON string
update_site_instance = UpdateSite.from_json(json)
# print the JSON string representation of the object
print(UpdateSite.to_json())

# convert the object into a dict
update_site_dict = update_site_instance.to_dict()
# create an instance of UpdateSite from a dict
update_site_from_dict = UpdateSite.from_dict(update_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


