# EsignatureDocusignRecipientTab


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of Recipient | [optional] 
**page_number** | **str** | Document Page Number | [optional] 
**position_x** | **str** | Element X Position | [optional] 
**position_y** | **str** | Element Y Position | [optional] 

## Example

```python
from formkiq_client.models.esignature_docusign_recipient_tab import EsignatureDocusignRecipientTab

# TODO update the JSON string below
json = "{}"
# create an instance of EsignatureDocusignRecipientTab from a JSON string
esignature_docusign_recipient_tab_instance = EsignatureDocusignRecipientTab.from_json(json)
# print the JSON string representation of the object
print(EsignatureDocusignRecipientTab.to_json())

# convert the object into a dict
esignature_docusign_recipient_tab_dict = esignature_docusign_recipient_tab_instance.to_dict()
# create an instance of EsignatureDocusignRecipientTab from a dict
esignature_docusign_recipient_tab_form_dict = esignature_docusign_recipient_tab.from_dict(esignature_docusign_recipient_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


