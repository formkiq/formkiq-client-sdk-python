# OnlyOfficeConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**only_office_url** | **str** | URL of the ONLYOFFICE application | [optional] 
**token** | **str** | ONLYOFFICE security token | [optional] 
**document_type** | **str** | Type of document (https://api.onlyoffice.com/editors/config/) | [optional] 
**editor_config** | [**OnlyOfficeEditorConfig**](OnlyOfficeEditorConfig.md) |  | [optional] 
**document** | [**OnlyOfficeConfigDocument**](OnlyOfficeConfigDocument.md) |  | [optional] 

## Example

```python
from formkiq_client.models.only_office_config import OnlyOfficeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OnlyOfficeConfig from a JSON string
only_office_config_instance = OnlyOfficeConfig.from_json(json)
# print the JSON string representation of the object
print OnlyOfficeConfig.to_json()

# convert the object into a dict
only_office_config_dict = only_office_config_instance.to_dict()
# create an instance of OnlyOfficeConfig from a dict
only_office_config_form_dict = only_office_config.from_dict(only_office_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


