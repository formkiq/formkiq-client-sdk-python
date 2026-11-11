# DocusignTextTab

A text field supporting single-line and multiline entry. Use width and height to size a multiline field and maxLength to limit input. Reserve sufficient space in the generated document; tabs do not reflow surrounding content. disableAutoSize affects single-line fields only. Specify either anchorString (with optional anchor settings) or pageNumber, xPosition, and yPosition. Do not combine anchor and coordinate placement. Recipient and document assignment are inherited from the containing request.

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
**value** | **str** | Initial field value. Use locked to prevent recipient edits. | [optional] 
**required** | **str** | Whether the recipient must complete the field. When omitted, DocuSign defaults apply. | [optional] 
**locked** | **str** | When true, the recipient cannot edit the field. | [optional] 
**width** | **str** | Field width in pixels. | [optional] 
**validation_pattern** | **str** | DocuSign regular expression used to validate the entered value. | [optional] 
**validation_message** | **str** | Message shown when the entered value fails validation. | [optional] 
**height** | **str** | Field height in pixels. Set with width to size a multiline text area. | [optional] 
**max_length** | **str** | Maximum number of characters accepted by the field. | [optional] 
**disable_auto_size** | **str** | Disable automatic resizing of single-line text fields. This property does not enable multiline entry. | [optional] 
**font** | **str** | DocuSign font name. | [optional] 
**font_size** | **str** | DocuSign font size, for example Size12. | [optional] 
**font_color** | **str** | DocuSign font color name, for example Black. | [optional] 
**bold** | **str** | Whether the field text is bold. | [optional] 
**italic** | **str** | Whether the field text is italic. | [optional] 
**underline** | **str** | Whether the field text is underlined. | [optional] 

## Example

```python
from formkiq_client.models.docusign_text_tab import DocusignTextTab

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignTextTab from a JSON string
docusign_text_tab_instance = DocusignTextTab.from_json(json)
# print the JSON string representation of the object
print(DocusignTextTab.to_json())

# convert the object into a dict
docusign_text_tab_dict = docusign_text_tab_instance.to_dict()
# create an instance of DocusignTextTab from a dict
docusign_text_tab_from_dict = DocusignTextTab.from_dict(docusign_text_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


