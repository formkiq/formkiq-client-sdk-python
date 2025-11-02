# DocusignSignHereTabs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor_string** | **str** | Specifies the string to find in the document and use as the basis for tab placement. | [optional] 
**anchor_x_offset** | **str** | Specifies the X axis location of the tab in anchorUnits relative to the anchorString. | [optional] 
**anchor_y_offset** | **str** | Specifies the Y axis location of the tab in anchorUnits relative to the anchorString. | [optional] 
**anchor_ignore_if_not_present** | **str** | When true, this tab is ignored if the anchorString is not found in the document. | [optional] 
**anchor_units** | **str** | Specifies units of the anchorXOffset and anchorYOffset | [optional] 
**x_position** | **str** | This property indicates the horizontal offset of the object on the page | [optional] 
**y_position** | **str** | This property indicates the vertical offset of the object on the page | [optional] 
**page_number** | **str** | Specifies the page number on which the tab is located | [optional] 

## Example

```python
from openapi_client.model.docusign_sign_here_tabs import DocusignSignHereTabs

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignSignHereTabs from a JSON string
docusign_sign_here_tabs_instance = DocusignSignHereTabs.from_json(json)
# print the JSON string representation of the object
print(DocusignSignHereTabs.to_json())

# convert the object into a dict
docusign_sign_here_tabs_dict = docusign_sign_here_tabs_instance.to_dict()
# create an instance of DocusignSignHereTabs from a dict
docusign_sign_here_tabs_from_dict = DocusignSignHereTabs.from_dict(docusign_sign_here_tabs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


