# SiteUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_count** | **float** | The number of documents in the site (only tracked when using MaxDocuments) | [optional] 
**ocr_transaction_count** | **float** | The number of ocr tx requests in the site (only tracked when using OCR MaxTransactions) | [optional] 

## Example

```python
from openapi_client.models.site_usage import SiteUsage

# TODO update the JSON string below
json = "{}"
# create an instance of SiteUsage from a JSON string
site_usage_instance = SiteUsage.from_json(json)
# print the JSON string representation of the object
print(SiteUsage.to_json())

# convert the object into a dict
site_usage_dict = site_usage_instance.to_dict()
# create an instance of SiteUsage from a dict
site_usage_from_dict = SiteUsage.from_dict(site_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


