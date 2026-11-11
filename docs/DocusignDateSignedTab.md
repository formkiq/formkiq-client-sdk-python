# DocusignDateSignedTab

An automatic signing date populated by DocuSign when the recipient signs. The caller cannot set its value. Date and time formatting follow DocuSign account settings. Specify either anchorString (with optional anchor settings) or pageNumber, xPosition, and yPosition. Do not combine anchor and coordinate placement. Recipient and document assignment are inherited from the containing request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor_string** | **str** | Text used to locate the tab. Every matching occurrence creates a tab. Use distinct anchors for different recipients. | [optional] 
**anchor_x_offset** | **str** | Horizontal offset from the anchor in anchorUnits; negative offsets are allowed. | [optional] 
**anchor_y_offset** | **str** | Vertical offset from the anchor in anchorUnits; negative offsets are allowed. | [optional] 
**anchor_units** | **str** | Units for anchor offsets. | [optional] 
**anchor_ignore_if_not_present** | **str** | When true, omit the tab if its anchor is missing. When false, a missing anchor is an error. When omitted, DocuSign defaults apply. | [optional] 
**anchor_case_sensitive** | **str** | Whether anchor matching is case sensitive. When omitted, DocuSign defaults apply. | [optional] 
**anchor_match_whole_word** | **str** | Whether the anchor must match a whole word. When omitted, DocuSign defaults apply. | [optional] 
**page_number** | **str** | One-based page number for coordinate placement. | [optional] 
**x_position** | **str** | Horizontal position in pixels for coordinate placement. | [optional] 
**y_position** | **str** | Vertical position in pixels for coordinate placement. | [optional] 
**tab_label** | **str** | Field label used to identify the tab. | [optional] 
**font** | **str** | DocuSign font name. | [optional] 
**font_size** | **str** | DocuSign font size, for example Size12. | [optional] 
**font_color** | **str** | DocuSign font color name, for example Black. | [optional] 
**bold** | **str** | Whether the field text is bold. | [optional] 
**italic** | **str** | Whether the field text is italic. | [optional] 
**underline** | **str** | Whether the field text is underlined. | [optional] 

## Example

```python
from formkiq_client.models.docusign_date_signed_tab import DocusignDateSignedTab

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignDateSignedTab from a JSON string
docusign_date_signed_tab_instance = DocusignDateSignedTab.from_json(json)
# print the JSON string representation of the object
print(DocusignDateSignedTab.to_json())

# convert the object into a dict
docusign_date_signed_tab_dict = docusign_date_signed_tab_instance.to_dict()
# create an instance of DocusignDateSignedTab from a dict
docusign_date_signed_tab_from_dict = DocusignDateSignedTab.from_dict(docusign_date_signed_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


