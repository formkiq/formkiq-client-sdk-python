# DocusignSigningTabs

Recipient tabs for both signers and inpersonSigners. Each tab belongs to the containing recipient and the document or artifact selected by this endpoint; FormKiQ assigns DocuSign documentId \"1\". Per-tab recipientId and documentId overrides are unsupported. Supported collections are signHereTabs, initialHereTabs, dateSignedTabs, dateTabs, and textTabs. Checkboxes, radio groups, dropdowns, name/email/company/title/number fields, conditional fields, formulas, attachments, payments, approve/decline controls, and other collections are not supported by this contract. Unknown collections and properties are ignored during request deserialization, consistent with other FormKiQ requests. Supported field values and placement are validated after deserialization. Existing signature properties retain their types and optionality. Completed field-value retrieval is outside this request contract. Support tracking: https://github.com/formkiq/formkiq-platform/issues/277.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_here_tabs** | [**List[DocusignSignHereTabs]**](DocusignSignHereTabs.md) | Signature fields; preserves the existing signature request format. | [optional] 
**initial_here_tabs** | [**List[DocusignInitialHereTab]**](DocusignInitialHereTab.md) | Recipient initials. | [optional] 
**date_signed_tabs** | [**List[DocusignDateSignedTab]**](DocusignDateSignedTab.md) | Automatic signing dates. | [optional] 
**date_tabs** | [**List[DocusignDateTab]**](DocusignDateTab.md) | Recipient-entered dates. | [optional] 
**text_tabs** | [**List[DocusignTextTab]**](DocusignTextTab.md) | Single-line or multiline text fields. | [optional] 

## Example

```python
from formkiq_client.models.docusign_signing_tabs import DocusignSigningTabs

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignSigningTabs from a JSON string
docusign_signing_tabs_instance = DocusignSigningTabs.from_json(json)
# print the JSON string representation of the object
print(DocusignSigningTabs.to_json())

# convert the object into a dict
docusign_signing_tabs_dict = docusign_signing_tabs_instance.to_dict()
# create an instance of DocusignSigningTabs from a dict
docusign_signing_tabs_from_dict = DocusignSigningTabs.from_dict(docusign_signing_tabs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


