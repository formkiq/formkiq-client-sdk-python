# OnlyOfficeConfigDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Defines the absolute URL where the source viewed or edited document is stored | [optional] 
**title** | **str** | Defines the desired file name for the viewed or edited document | [optional] 
**key** | **str** | Defines the unique document identifier used by the service to recognize the document | [optional] 
**file_type** | **str** | Defines the type of the file for the source viewed or edited document | [optional] 

## Example

```python
from formkiq_client.models.only_office_config_document import OnlyOfficeConfigDocument

# TODO update the JSON string below
json = "{}"
# create an instance of OnlyOfficeConfigDocument from a JSON string
only_office_config_document_instance = OnlyOfficeConfigDocument.from_json(json)
# print the JSON string representation of the object
print OnlyOfficeConfigDocument.to_json()

# convert the object into a dict
only_office_config_document_dict = only_office_config_document_instance.to_dict()
# create an instance of OnlyOfficeConfigDocument from a dict
only_office_config_document_form_dict = only_office_config_document.from_dict(only_office_config_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


