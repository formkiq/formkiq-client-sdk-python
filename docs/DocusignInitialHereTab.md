# DocusignInitialHereTab

A field for recipient initials. Specify either anchorString (with optional anchor settings) or pageNumber, xPosition, and yPosition. Do not combine anchor and coordinate placement. Recipient and document assignment are inherited from the containing request.

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
**optional** | **str** | Whether the recipient may leave the initials field empty. | [optional] 
**scale_value** | **str** | Positive scaling factor for the initials field. | [optional] 

## Example

```python
from formkiq_client.models.docusign_initial_here_tab import DocusignInitialHereTab

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignInitialHereTab from a JSON string
docusign_initial_here_tab_instance = DocusignInitialHereTab.from_json(json)
# print the JSON string representation of the object
print(DocusignInitialHereTab.to_json())

# convert the object into a dict
docusign_initial_here_tab_dict = docusign_initial_here_tab_instance.to_dict()
# create an instance of DocusignInitialHereTab from a dict
docusign_initial_here_tab_from_dict = DocusignInitialHereTab.from_dict(docusign_initial_here_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


