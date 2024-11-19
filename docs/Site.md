# Site


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **str** | Site Identifier | [optional] 
**title** | **str** | Site Title | [optional] 
**status** | [**SiteStatus**](SiteStatus.md) |  | [optional] 
**permission** | **str** | SiteId permission level | [optional] 
**permissions** | [**List[SiteGroupPermissions]**](SiteGroupPermissions.md) |  | [optional] 
**upload_email** | **str** | SiteId document upload email address | [optional] 

## Example

```python
from formkiq_client.models.site import Site

# TODO update the JSON string below
json = "{}"
# create an instance of Site from a JSON string
site_instance = Site.from_json(json)
# print the JSON string representation of the object
print(Site.to_json())

# convert the object into a dict
site_dict = site_instance.to_dict()
# create an instance of Site from a dict
site_from_dict = Site.from_dict(site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


